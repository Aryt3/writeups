# QR-code

## Description
```
The flag is hidden in QR codes

nc ctf.mf.grsu.by 9011
```

## Writeup

Now connecting to the service I received a QR-code in the form of a `base64` encoded string. <br/>
Now the challenge was simply to convert the base64 string into an image so we have an actual QR-code which we can scan. After that we need to scan the QR-code to get the content of the QR-code. <br/>
For this purpose I first coded an endpoint to scan QR-codes. <br/>
```js
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
```
Now this `express.js/node.js` endpoint is able to get image files and return the output of a QR-code.

```py
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route("/decodeQR", methods=["POST"])
def decode_qr():
    try:
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(f"uploads/{filename}")

            image = Image.open(f"uploads/{filename}")
            decoded_data = decode(image)

            if decoded_data:
                result = decoded_data[0].data.decode("utf-8")
                return result
            else:
                return jsonify({"error": "No QR code found in the image"})

        else:
            return jsonify({"error": "No file uploaded"})

    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
This `Flask` endpoint is doing the same thing as the `express.js` endpoint. <br/>

```py
import socket, re, base64, time, requests

def img(base64_string):
    imgdata = base64.b64decode(base64_string)
    with open('img.jpg', 'wb') as f:
        f.write(imgdata)
        
    time.sleep(0.5)

    files = {'file': open('img.jpg', 'rb')}  

    response = requests.post('http://127.0.0.1:3000/decodeQR', files=files)

    if response.text == 'error':
        imgdata = base64.b64decode(base64_string)
        with open('img.jpg', 'wb') as f:
            f.write(imgdata)

        time.sleep(0.5)

        files = {'file': open('img.jpg', 'rb')}  

        response = requests.post('http://127.0.0.1:5000/decodeQR', files=files)

    return response.text

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("ctf.mf.grsu.by", 9011))
        found_flag = False 

        while True:
            data = s.recv(1024).decode()
            print(data)

            if "grodno{" in data:
                found_flag = True
                break

            if not found_flag: 
                cur_code = ''
                check = False               
                split_data = data.split()

                for char in split_data:
                    if check == True:
                        cur_code += char

                    if re.search(r'\d+/\d+', char):
                        check = True

                answer = img(cur_code)
                print(answer)

                if answer and 'Error' not in answer and 'No QR' not in answer:
                    s.send(f"{answer}\n".encode())
                    time.sleep(0.5)
                else:
                    print("Failed to decode QR code. Sending empty answer.")
                    break

if __name__ == "__main__":
    main()
```

This script is the main script to solve the challenge. <br/>
It initiates a socket connection to the service and uses the QR-code scanning endpoints to read the output from the base64 strings. <br/>
I used 2 different endpoints because with 1 it didn't quite work because some QR-codes seemed to be faulty. <br/>
Executing the scripts above I was able to obtain the flag which concludes this writeup. <br/>
```sh
kali@kali python3 solver.py
Все что тебе надо - найти QR-код с флагом. И так раз 50 ...
Время на ответ - не больше 5 секунд ...

Раунд 1/57
----------------------------------------------------

introduction_&_invasion_&_invest
Правильно: introduction_&_invasion_&_invest
grodno{71e5e0_d3c0d3_&_fr0m_&_QR_bf08a6}
```