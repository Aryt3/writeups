# Site Map

## Description
```
http://ctf.mf.grsu.by/tasks/0448a5c387935239c9fa6e7d20f0c50f/
```

## Writeup

Now the challenge name sounds oddly familiar, `sitemap.xml` is a common file found in a lot of websites and web frameworks. <br/>
Knowing this I just went to `http://ctf.mf.grsu.by/tasks/0448a5c387935239c9fa6e7d20f0c50f/sitemap.xml` which was actually where the flag was located at. <br/>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.grsu.by/</loc>
        <priority>grodno{kesZvFNxwP67ZyQtX0Pb}</priority>
    </url>
</urlset>
```

This could have been found by a directory scan but is kind of unnecessary if you know basic web files. 