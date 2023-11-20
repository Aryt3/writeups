# Easy as it Gets

## Description
```
It doesn't get much easier than this when it comes to reverse engineering. 
Here we have a "secure" PowerShell script. 
All you need to do is figure out the super secret passphrase to decrypt the flag. 
```

## Provided Files
`RE1.ps1`

## Writeup

Taking a look at the provided script. <br/>
```ps1
[Reflection.Assembly]::LoadWithPartialName("System.Security")  

function Encrypt-String($String, $Passphrase, $salt="SaltCrypto", $init="IV_Password", [switch]$arrayOutput)  
{  
    $r = new-Object System.Security.Cryptography.RijndaelManaged  
    $pass = [Text.Encoding]::UTF8.GetBytes($Passphrase)  
    $salt = [Text.Encoding]::UTF8.GetBytes($salt)  
    $r.Key = (new-Object Security.Cryptography.PasswordDeriveBytes $pass, $salt, "SHA1", 5).GetBytes(32) #256/8  
    $r.IV = (new-Object Security.Cryptography.SHA1Managed).ComputeHash( [Text.Encoding]::UTF8.GetBytes($init) )[0..15]  
    $c = $r.CreateEncryptor()  
    $ms = new-Object IO.MemoryStream  
    $cs = new-Object Security.Cryptography.CryptoStream $ms,$c,"Write"  
    $sw = new-Object IO.StreamWriter $cs  
    $sw.Write($String)  
    $sw.Close()  
    $cs.Close()  
    $ms.Close()  
    $r.Clear()  
    [byte[]]$result = $ms.ToArray()  
    return [Convert]::ToBase64String($result)  
}  
  
function Decrypt-String($Encrypted, $Passphrase, $salt="SaltCrypto", $init="IV_Password")  
{  
    if($Encrypted -is [string]){  
        $Encrypted = [Convert]::FromBase64String($Encrypted)  
    }  

    $r = new-Object System.Security.Cryptography.RijndaelManaged  
    $pass = [Text.Encoding]::UTF8.GetBytes($Passphrase)  
    $salt = [Text.Encoding]::UTF8.GetBytes($salt)  
    $r.Key = (new-Object Security.Cryptography.PasswordDeriveBytes $pass, $salt, "SHA1", 5).GetBytes(32) #256/8  
    $r.IV = (new-Object Security.Cryptography.SHA1Managed).ComputeHash( [Text.Encoding]::UTF8.GetBytes($init) )[0..15]  
    $d = $r.CreateDecryptor()  
    $ms = new-Object IO.MemoryStream @(,$Encrypted)  
    $cs = new-Object Security.Cryptography.CryptoStream $ms,$d,"Read"  
    $sr = new-Object IO.StreamReader $cs  

    Write-Output $sr.ReadToEnd()  

    $sr.Close()  
    $cs.Close()  
    $ms.Close()  
    $r.Clear()  
}  

cls  

#### 
# TODO: use strong password
# Canadian_Soap_Opera
### 

$pwd = read-host "(Case Sensitive) Please Enter User Password"  

$pcrypted = "TTpgx3Ve2kkHaFNfixbAJfwLqTGQdk9dkmWJ6/t0UCBH2pGyJP/XDrXpFlejfw9d"  

write-host "Encrypted Password is: $pcrypted"  
write-host ""  
write-host "Testing Decryption of Username / Password..."  
write-host ""      

$pdecrypted = Decrypt-String $pcrypted $pwd 

write-host "Decrypted Password is: $pdecrypted"  
```

Some interesting stuff, especially the comments. <br/>
Anyway let's just execute the script with windows powershell (ps1 script is for powershell). <br/>
```sh
PS C:\Users\W1sh\Desktop> .\RE1.ps1

(Case Sensitive) Please Enter User Password: Canadian_Soap_Opera
Encrypted Password is: TTpgx3Ve2kkHaFNfixbAJfwLqTGQdk9dkmWJ6/t0UCBH2pGyJP/XDrXpFlejfw9d

Testing Decryption of Username / Password...

Decrypted Password is: poctf{uwsp_4d_v1c70r14m_w4573l4nd3r}
```

Getting the prompt I just used the password from the comment I found in the file, this finishes this challenge. <br/>
