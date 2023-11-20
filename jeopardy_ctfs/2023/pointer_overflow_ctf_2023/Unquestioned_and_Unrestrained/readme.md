# Unquestioned and Unrestrained

## Description:
```
First crypto challenge so we have to keep it easy. 
Here's the flag, but it's encoded. 
All you have to do is figure out which method was used. Luckily, it's a common one. 
```

## Provided string:
```
cG9jdGZ7dXdzcF80MTFfeTB1Ml84NDUzXzQyM184MzEwbjlfNzBfdTV9
```

## Writeup

Now I instantly thought that this looks like a Base64 encoded String. <br/>
Inputing the string into CyberChef and adding the magic module I instantly get the flag which was actually base64 encoded. <br/>

Flag: `poctf{uwsp_411_y0u2_8453_423_8310n9_70_u5}`
