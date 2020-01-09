import serial

while True :
    txt = input("BARCODE SCANNER: ")
    ser = serial.Serial('COM4', 115200)
    ser.write(b'3')
    ser.close()

