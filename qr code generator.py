import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=LmcWMjBpYBU")
img.save("qrcode.png")
