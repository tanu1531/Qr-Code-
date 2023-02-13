import qrcode 



qr = qrcode.QRCode(version=1, box_size=10,border=4,)
qr.add_data('https://www.youtube.com/watch?v=RsN0aXfPR1E')
qr.make(fit=True)
img = qr.make_image(fill_color="blue",
                    back_color="white")
img.save("col.png")