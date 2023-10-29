# Unhackable Andy

## Description
```
Someone might want to let ol' Andy know the old addage - pride goeth before the fall. 
```

## Writeup

Taking a look at the website.
![grafik](https://github.com/Aryt3/writeups/assets/110562298/535bfd3e-e26a-482f-8ce2-e396ed9a4d07)

Nothing of interest on the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/e72adace-2c3c-456b-bec9-5a2e3f6aa393)

Before looking further into exploiting the login I saw that there is a guthub link on the homepage. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/8eea503b-2c97-4b26-b0f1-21a1c8c9535e)

The user seems to have 2 respositories. Checking out the the first on I found the message `My other site, the one I made after "the incident."`. <br/>
To me this would indicate a password leak or any other kind of misshap. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/05d54d18-bd5b-48ae-96ee-2d5d9beb6d9e)

Taking a look at the commit history of the other repository I found a commit named `Create .env`. <br/>
Now this may be interesting because a `.env` file normally stores sensitive information. <br/>
```env
ADMIN_USERNAME=unhackableandy
ADMIN_PASSWORD=ThisIsASUPERStrongSecuredPasswordAndIAMUNHACKABLEANDYYYYBOIIIII133742069LOLlolLOL
```

Seems like he uploaded credentials. Remembering that there was a login interface on the website I pasted them into it. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/34fc8779-9e15-4577-8554-63b0336f5275)

After gaining access to the dashboard I instantly see an input field pre-filled with a linux command. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/07eb89eb-767b-4211-ba1a-e2e8c1f66f25)

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


