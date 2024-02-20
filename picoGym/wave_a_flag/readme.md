# Wave a flag

## Description
```
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...
```

## Provided Files
```
- warm
```

## Writeup

When reading this challenge description you should realize that this is about a `binary`. <br/>
A `binary` is simply an executable file, often created through compilation, which scrambles the original code to make it less readable. <br/>
We can execute a `binary` in any linux terminal. <br/>
```sh
$ ./warm    
Hello user! Pass me a -h to learn what I can do!
```

Seeing that we are basically asked to add the parameter `-h` to the `binary` we can simply do that. <br/>
```sh
./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_6635aa47}
```

Doing that reveals the flag to us which concludes this writeup. <br/>

> [!NOTE]
> If we have such a text in a file we can also try to search the file for `strings`.
> There is a simple linux utility to do exactly that. `strings FILE`

Try it out on a file. <br/>
```sh
$ strings warm

--------------------

Hello user! Pass me a -h to learn what I can do!
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_6635aa47}
I don't know what '%s' means! I do know what -h means though!

--------------------
```

This way we could have also solved this challenge.