#pip install qrcode
import qrcode
#data you want the qr code to display
data = 'Follow me on TikTok : cloanic'

# img = qrcode.make(data)

# print("What directory will you want the qr code saved?")
# named_directory = input("Directory: ")
# img.save('named_directory'+'/myqrcode.png')
#customize the qr code
qr = qrcode.QRCode(version = 1, box_size=10, border = 5)
#add the data to the qr code
qr.add_data(data)
#make the qr code with differnet colors
qr.make(fit=True)
img = qr.make_image(fill_color = 'orange', back_color = 'white')
#input a directory from a user
named_directory = input("Directory: ")
#save the qr code to the directory as myqrcode.png
img.save('named_directory'+'/myqrcode.png')