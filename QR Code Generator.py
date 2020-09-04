import pyqrcode
import png

str = "String which represent the QR Code message or the reference link"

gen = pyqrcode.create(str)  #Generating QR Code

gen.svg("myqrcode.svg", scale = 8 ) #Saving the qrcode generated in svg file

gen.png("myqrcode.png", scale = 8) #Saving the qrcode generated in png file.
