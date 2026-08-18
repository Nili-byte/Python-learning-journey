import qrcode as qr

# msg = qr.make("https://github.com/python-telegram-bot/python-telegram-bot")

# # msg.save("test.png")

# adven = qr.QRCode(version=1,box_size=16,border=4)
# adven.add_data("https://claude.ai/")
# adven.make(fit=True)
# f = adven.make_image(fill_color = "red" , back_color = "yellow")
# f.save("test2.png")



url = input("Enter url or text to make QR.. : ")

print("Normal QR ==> 1")
print("Custom QR ==> 0")
# choice = int(input("Enter your QRCODE Type : "))
while True:
    try:
        choice = int(input("Enter your QRCODE Type : "))
        if choice in (0,1):
         break
        else:
         print("Invalid try again , only 0/1 is accepted : ")
    except ValueError:
     print("Invalid ! only 0/1 is accepted : ")

nf = input("Enter your QRcode file name :")
nff = (f"{nf}.png")


if(choice == 1):
  w1 = qr.make(f"{url}")
  w1.save(f"{nff}")


else:
  color = input("Enter your qrcode colour name coded one : ")
  bkcolor = input("Enter your qrcode background colour name: ")

  c = qr.QRCode(version=1 , border=4)
  c.add_data(f"{url}")
  c.make(fit=True)
  img = c.make_image(fill_color = color,back_color = bkcolor)
  
  img.save(f"{nff}")

print(" ")

print("The QRcode is been sucessfully generated and has been as",nff)

  
   
