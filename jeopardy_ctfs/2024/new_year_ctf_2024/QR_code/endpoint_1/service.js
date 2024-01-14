const express = require('express');
const multer = require('multer');
const Jimp = require('jimp');
const QrCode = require('qrcode-reader');

const app = express();
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.post('/decodeQR', upload.single('file'), (req, res) => {
    try {
        const imageBuffer = req.file.buffer;

        Jimp.read(imageBuffer, (err, image) => {
            if (err) {
                res.send('error')
            }

            const qr = new QrCode();
            qr.callback = (err, value) => {
                if (value && value.result) {
                    console.log(value.result);
                } else {
                    console.log("Result not available or undefined");
                }
                if (err) {
                    res.send('error')
                } else {
                    res.send(value.result)
                }
            };

            qr.decode(image.bitmap);
        });
    } catch (error) {
        res.send('error')
    }
});

app.listen(3000, '0.0.0.0', () => {
    console.log(`Server is running on http://0.0.0.0:3000`);
});