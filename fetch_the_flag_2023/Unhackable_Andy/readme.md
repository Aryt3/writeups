# Unhackable Andy

## Description
```
Someone might want to let ol' Andy know the old addage - pride goeth before the fall. 
```

## Writeup

Taking a look at the website.
![grafik](https://github.com/Aryt3/writeups/assets/110562298/0a6329cf-a665-46f2-8e90-73d4adbfce61)

Nothing of interest on the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/5181d0b5-3ef8-4fe8-8f33-c99a599202c0)

Before looking further into exploiting the login I saw that there is a guthub link on the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/045d8416-56d5-4ff1-b96a-14756283b9cb)

The user seems to have 2 respositories. Checking out the the first on I found the message `My other site, the one I made after "the incident."`. <br/>
To me this would indicate a password leak or any other kind of misshap. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/4060b408-2ab4-45fc-97ad-03bed4c9534f)

Taking a look at the commit history of the other repository I found a commit named `Create .env`. <br/>
Now this may be interesting because a `.env` file normally stores sensitive information. <br/>
```env
ADMIN_USERNAME=unhackableandy
ADMIN_PASSWORD=ThisIsASUPERStrongSecuredPasswordAndIAMUNHACKABLEANDYYYYBOIIIII133742069LOLlolLOL
```

Seems like he uploaded credentials. Remembering that there was a login interface on the website I pasted them into it. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/54bf2feb-7dfa-4c32-9cbe-acbb4107df86)

After gaining access to the dashboard I instantly see an input field pre-filled with a linux command. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/695ef6f6-3413-4d24-be95-7d388b147dd4)

After executing a simple linux command I knew for sure. The last thing to do now is finding the flag. <br/>
```sh
$ whoami
root
$ find / | grep flag
/sys/devices/pnp0/00:05/tty/ttyS2/flags
/sys/devices/pnp0/00:03/tty/ttyS0/flags
/sys/devices/pnp0/00:06/tty/ttyS3/flags
/sys/devices/pnp0/00:04/tty/ttyS1/flags
/sys/devices/virtual/net/eth0/flags
/sys/devices/virtual/net/lo/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/proc/sys/kernel/acpi_video_flags
/proc/sys/net/ipv4/fib_notify_on_flag_change
/proc/sys/net/ipv6/fib_notify_on_flag_change
/proc/kpageflags
/app/flag.txt
$ cat /app/flag.txt
flag{e81b8885d8a5e8d57bbadeb124cc956b}
```

After knowing that I was root I simply searched the whole filesystem for the flag and finally found and displayed it which finishes this challenge.


