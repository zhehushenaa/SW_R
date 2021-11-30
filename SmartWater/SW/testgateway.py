import serial
from time import sleep
import struct

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data


if __name__ == '__main__':
    # serial = serial.Serial('COM12', 115200, timeout=0.5)  # /dev/ttyUSB0
    # # senddata='\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55'
    # # ser.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')
    #
    # if serial.isOpen():
    #     print("open success")
    # else:
    #     print("open failed")
    #
    # serial.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')
    # data = serial.readall()
    # print (data)
    # serial.close()

    a = struct.pack("I", b)
    print (a)
    b = struct.unpack("I", a)

    print (b)