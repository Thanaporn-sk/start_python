#pip install pyqrcode
#pip install pypng



import pyqrcode

qrcode = pyqrcode.create('Hello my qrcode')
qrcode.png('hello.png',scale=7)
