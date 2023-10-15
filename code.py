import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=4)

link=input("Enter link here: ")
qr.add_data(link)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("qr.png")