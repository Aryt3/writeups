# Access Intel

## Introduction
```
This is an OSINT CTF challenge. You have been given a task to find the admin's ID, who joined the organization on an unknown date.
Unfortunately, the information you have been given is mixed up, and the admin is currently on the run.
The admin has a habit of wearing wrong pair of socks all the time.

You will need to find out the right combination of the following numbers to determine the date.

-49.4259871 / -49.2586095 / -49.4302086 / 70.5904309 / 70.3663355 / 70.3550075
```

## Goal
```
Find the ID of the admin of an organization
```

## Task
```
Can you use the numbers above and any other information you can find to get the admins' ID
```

## Flag Format
`HL{{7...}`

## Writeup

Starting off I thought that the numbers might be coordinates. <br/>
Knowing that I can input coordinates in google maps I just did that. <br/>

So inputing the coordinates `-49.4259871 70.5904309` we receive nothing. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/b2153a65-e3cd-48ca-bdd0-e0700044072b)

After switching around some more I received this. <br/>
![Untitled(9)](https://github.com/Aryt3/writeups/assets/110562298/e889490a-62eb-4fab-ac5b-9a1cc0f3bd24)

Searching for the name in the picture I receive this. <br/>
![Untitled(10)](https://github.com/Aryt3/writeups/assets/110562298/03a0db98-973b-4873-b644-65f9c82c8aef)

Looking at the comments I see a very strange text. <br/>
![Untitled(11)](https://github.com/Aryt3/writeups/assets/110562298/58952855-0b30-4803-8210-7b847cab45a1)

It almost looks like a caesar cipher. Knowing this I did a bruteforce on caesar cipher and obtained the following. <br/>
```
Discord Admin is still hiding here RggGV52VeT
```

If the discord server is public we can use `RggGV52VeT` to join the discord server entering the URL `https://discord.gg/RggGV52VeT` in a browser or in discord. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/7d92fb29-a654-41a5-aa67-00ee7ee4972d)

Joining the server we can see somebody seems to have a more important role than others marked by the color of their username. <br/>
Doing a small right click on the account of the admin we have the following options. <br/>
![grafik](https://github.com/Aryt3/writeups/assets/110562298/bb720b69-cc62-4420-9c95-e5cd03794f25)

> [!NOTE]
> You only have those options if you enabled developer mode in discord.

Copying his User ID we obtain `708403267893329951` which concludes this challenge. 
