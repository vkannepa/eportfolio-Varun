"""
generate_qr.py — regenerate qr-code.png whenever the URL changes.

Install dependency:
    pip install qrcode[pil]

Usage:
    python generate_qr.py
"""

import qrcode

URL = "https://github.com/AVHBAC/undergrad-eportfolio-tutorial"

qr = qrcode.QRCode(
    version=None,          # auto-size
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")
print(f"QR code saved to qr-code.png  →  {URL}")
