import serial
from time import sleep
import struct

import binascii

# def recv(serial):
#     while True:
#         data = serial.read_all()
#         if data == '':
#             continue
#         else:
#             break
#         sleep(0.02)
#     return data
#
#
# if __name__ == '__main__':
#     serial = serial.Serial('COM12', 115200, timeout=0.5)  # /dev/ttyUSB0
#     # senddata='\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55'
#     # ser.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')
#
#     if serial.isOpen():
#         print("open success")
#     else:
#         print("open failed")
#
#     serial.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')
#     data = serial.readall()
#     print (data)
#     serial.close()
#     ss=data
#     # ss= b'\xaa\xaaB\xc4\xc1\xee\xef\xb8qA(\x03P\x00\xf4\xfd\xd4;\x14\x01\x01\x04#\xb8\x0b \xc7\x02\x00\x00[\x00\x00\x00\x00\x00\x00\x00\xef\xb8qA0\x03P\x00\n\xd7\xa3<\x14\x01\x01\x04"\x90e \xc7\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00\xef\xb8qA8\x03P\x00?5~\xbf\x14\x01\x01\x04 \x88\x90 \xc7\x02\x00\x00W\x00\x00\x00\x00\x00\x00\x00\xd4SqA(\x00P\x00\x00\x00\xc0A\x14\x01\x01\x04#(#\x00\xc6\x02\x00\x00P\x00\x00\x00\x00\x00\x00\x00\xfbEqA(\x00P\x00\x00\x00\xb8A\x14\x01\x01\x04#\xe0\xab\x00\xc6\x02\x00\x00T\x00\x00\x00\x00\x00\x00\x00\x19\xa8qA(\x00P\x00\x00\x00\xb0A\x14\x01\x01\x04#\xd8Y \xca\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00$\xa0UU'
#     # ss=b'\xaa\xaaB\xc4A\xee\xfbEqA(\x00P\x00\x00\x00\xb8A\x14\x01\x01\x05\x08X\x1b\x00\xc6\x02\x00\x00Q\x00\x00\x00\x00\x00\x00\x00\x19\xa8qA\x00\x03P\x00\x00J\xc7G\x14\x01\x01\x05\x05(# \xca\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00\x9a\xfbUU'
#
#
#     # data = '00 00 AC 41'
#     # fdata = struct.unpack('<f', binascii.unhexlify(data.replace(' ', '')))[0]
#     # print(fdata)
#     #
#     # data1 = '0000AC41'
#     # fdata = struct.unpack('<f', binascii.unhexlify(data1))[0]
#     # print("变换",str(fdata))
#
#     # a=b'\xaaB'
#     # a = struct.pack("2I", 12, 34)
#     # print (a)
#
#     # b = struct.unpack("2I", a)
#     #
#     # print (b)
#
#     print (ss[4:5])
#     print (len(ss))
#     n = int.from_bytes(ss[4:5], byteorder='little', signed=False)
#     print (n)
#     if n>1:
#         dataall = ss[6:]
#         print("检测到传感器数量：",str((n-1)/32))
#         for i in range(int((n-1)/32)):
#             data=dataall[:32]
#             dataall=dataall[32:]
#             print (data)
#             ID=data[:8]
#             value=data[8:12]
#             value=binascii.b2a_hex(value).decode('utf-8')
#             print (ID)
#             # ID=b'\x5A\xA5'
#             print ("传感器ID：",binascii.b2a_hex(ID).decode('utf-8'))
#             value = struct.unpack('<f', binascii.unhexlify(value))[0]
#             print("传感器数值：",str(value) )
#             # str1 = ID.decode('UTF-8')
#
#
#             # print("str1: ", str1)

global oldc
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def hu():

    # dict1 = {}
    dict2 = {'a': 20, 'c': 4}
    # if oldc=='none':
    #     print ("jjjjj")

    dict3 = Merge(oldc, dict2)
    print(dict3)
print ("huhuu")
hu()