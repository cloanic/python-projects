import qrcode

data = 'Follow me on TikTok : cloanic'

# img = qrcode.make(data)

# print("What directory will you want the qr code saved?")
# named_directory = input("Directory: ")
# img.save('named_directory'+'/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size=10, border = 5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'orange', back_color = 'white')

named_directory = input("Directory: ")
img.save('named_directory'+'/myqrcode.png')