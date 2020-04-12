import qrcode


# Hello world with qrcode
qr_1 = qrcode.make("hello world")
qr_1.save("myQR.png")


qr_2 = qrcode.QRCode(version=1, box_size=15, border=5)

data = "https://www.google.com.br"
qr_2.add_data(data)
qr_2.make(fit=True)
img = qr_2.make_image(fill="black", black_color="white")
img.save("Google site qrcode.png")
