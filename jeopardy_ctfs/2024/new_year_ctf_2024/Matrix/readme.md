# Matrix

## Description
```
http://ctf.mf.grsu.by/tasks/0411d67d76390a705554da73a6d38492/
```

## Writeup

Taking a look at the website we see a loot of `0` and `1`. <br/>
![image](https://github.com/Aryt3/writeups/assets/110562298/e7644abc-afb7-47ff-adec-717cd5cbf784)

Now instead of taking a look at the assumably binary content I took a look around the website. <br/>
Looking at the `css` I found something interesting. <br/>
```css
b {
    color: #03A062 !important;
}
```

Deleting this statement in its entirety I obtained the flag which concludes this writeup. <br/>
![image-1](https://github.com/Aryt3/writeups/assets/110562298/31a351b1-48db-486e-907b-bd41bc80339b)
