const express = require('express');
const puppeteer = require('puppeteer');

const randomBytes = require('crypto').randomBytes(32).toString('hex');

const fs = require('fs');

const flag = process.env.FLAG || fs.readFileSync('./flag', 'utf8');
const script = fs.readFileSync('./script.js', 'utf8');

const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(`
        <h1>TODO</h1>
        <form action="/chal" method="post">
            <input type="text" name="html" placeholder="HTML">
            <button type="submit">Submit to /chal</button>
        </form>
        <hr>
        <form action="/admin" method="post">
            <input type="text" name="html" placeholder="HTML">
            <button type="submit">Submit to /admin</button>
        </form>
    `);
});

app.post('/chal', (req, res) => {
    const { html } = req.body;
    res.setHeader("Content-Security-Policy", "default-src 'none'; script-src 'self' 'unsafe-inline';");
    res.send(`
        <script src="/script.js"></script>
        ${html}
    `);
});

app.get('/script.js', (req, res) => {
    res.type('.js');
    let response = script;
    if ((req.get("cookie") || "").includes(randomBytes)) response = response.replace(/GPNCTF\{.*\}/, flag)
    res.send(response);
});

app.post('/admin', async (req, res) => {
    try {
        const { html } = req.body;
        const browser = await puppeteer.launch({ executablePath: process.env.BROWSER, args: ['--no-sandbox'] });
        const page = await browser.newPage();
        page.setCookie({ name: 'flag', value: randomBytes, domain: 'localhost', path: '/', httpOnly: true });
        await page.goto('http://localhost:1337/');
        await page.type('input[name="html"]', html);
        await page.click('button[type="submit"]');
        await new Promise(resolve => setTimeout(resolve, 2000));
        const screenshot = await page.screenshot({ encoding: 'base64' });
        await browser.close();
        res.send(`<img src="data:image/png;base64,${screenshot}" />`);
    } catch(e) {console.error(e); res.send("internal error :( pls report to admins")}
});

app.listen(1337, () => console.log('listening on http://localhost:1337'));
