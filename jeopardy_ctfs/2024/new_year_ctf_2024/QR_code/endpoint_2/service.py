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