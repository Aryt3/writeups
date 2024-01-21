# Out of the Bucket

## Description
```
Check out my flag website!

Author: windex
```

## Writeup

Taking a look at the website. <br/>
```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Flags</title>
<meta name="generator" content="Jekyll v3.9.3" />
<meta property="og:title" content="Flags" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="website" />
<!-- End Jekyll SEO tag -->

    <link rel="stylesheet" href="https://storage.googleapis.com/out-of-the-bucket/src/static/style.css">
</head>

  <body>
    <div class="container-lg px-3 my-5 markdown-body">
      
      <h1>Flags</h1> 

      <h1>I love flags!</h1>

<p>I collect flags from all around the world. Here are some of my recent finds:</p>

<p>here's a flag i got while on a trip to antwerp!!</p>
<p><img width="700" src="https://storage.googleapis.com/out-of-the-bucket/src/static/antwerp.jpg"/></p>

<p>and here’s a flag from Guam:</p>
<p><img width="700" src="https://storage.googleapis.com/out-of-the-bucket/src/static/guam.jpg"/></p>
  
    </div>
  </body>
</html>
```

Looking at the root of the path `https://storage.googleapis.com/out-of-the-bucket/` it almost resembles a `sitemap.xml`. <br/>
```xml
<?xml version='1.0' encoding='UTF-8'?><ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
<Name>out-of-the-bucket</Name>
<Prefix></Prefix>
<Marker></Marker>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>secret/</Key>
<Generation>1703868492595821</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:48:12.634Z</LastModified>
<ETag>"d41d8cd98f00b204e9800998ecf8427e"</ETag>
<Size>0</Size>
</Contents>
<Contents>
<Key>secret/dont_show</Key>
<Generation>1703868647771911</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:50:47.809Z</LastModified>
<ETag>"737eb19c7265186a2fab89b5c9757049"</ETag><Size>29</Size>
</Contents>
<Contents>
<Key>secret/funny.json</Key>
<Generation>1705174300570372</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2024-01-13T19:31:40.607Z</LastModified>
<ETag>"d1987ade72e435073728c0b6947a7aee"</ETag>
<Size>2369</Size>
</Contents>
<Contents>
<Key>src/</Key>
<Generation>1703867253127898</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:27:33.166Z</LastModified>
<ETag>"d41d8cd98f00b204e9800998ecf8427e"</ETag>
<Size>0</Size>
</Contents>
<Contents>
<Key>src/index.html</Key>
<Generation>1703867956175503</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:39:16.214Z</LastModified>
<ETag>"dc63d7225477ead6f340f3057263643f"</ETag>
<Size>1134</Size>
</Contents>
<Contents>
<Key>src/static/antwerp.jpg</Key>
<Generation>1703867372975107</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:29:33.022Z</LastModified>
<ETag>"cef4e40eacdf7616f046cc44cc55affc"</ETag>
<Size>45443</Size>
</Contents>
<Contents>
<Key>src/static/guam.jpg</Key>
<Generation>1703867372954729</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:29:32.993Z</LastModified>
<ETag>"f6350c93168c2955ceee030ca01b8edd"</ETag>
<Size>48805</Size>
</Contents>
<Contents>
<Key>src/static/style.css</Key>
<Generation>1703867372917610</Generation>
<MetaGeneration>1</MetaGeneration>
<LastModified>2023-12-29T16:29:32.972Z</LastModified>
<ETag>"0c12d00cc93c2b64eb4cccb3d36df8fd"</ETag>
<Size>76559</Size>
</Contents>
</ListBucketResult>
```

There seem to be soem interesting paths there. <br/>
After looking through the `path` `/secret/` I was able to find something interesting. <br/>
```
https://storage.googleapis.com/out-of-the-bucket/secret/dont_show
```
Looking at this URL I found the flag which concludes this writeup. 