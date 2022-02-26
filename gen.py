import qrcode 
qr_img = qrcode.make("https://www.javatpoint.com/generate-a-qr-code-using-python")  
  
qr_img.save("qr-img.jpg")  
