import qrcode
while True:
    bgcolor= input('Enter Background Color:').lower()
    f_color= input('Enter Fill Color:').lower()
    data = input('Enter the text or URL:').strip()  #to remove any whitespace in link
    filename= input('Enter the filename:').strip()
    qr= qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    img= qr.make_image(fill_color=f_color, back_color=bgcolor)
    img.save(filename)
    print('QR code saved as {filename}')

    ch= input("Want to generate more QR? (y/n)").lower()
    if ch=='n':
        break
    else:
        continue