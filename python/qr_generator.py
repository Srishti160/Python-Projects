import qrcode
data = input('Enter the text or URL:').strip()  #to remove any whitespace in link
filename= input('Enter the filename:').strip()
qr= qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
img= qr.make_image(fill_color='black', back_color='white')
img.save(filename)
print('QR code saved as {filename}')