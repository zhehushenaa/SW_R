import serial
from time import sleep
import struct

import binascii

class gw_model:


    def __init__(self):
        self.serial = serial.Serial('COM12', 115200, timeout=0.5)  # /dev/ttyUSB0
        # senddata='\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55'
        # ser.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')

        # if self.serial.isOpen():
        #     print("open success")
        # else:
        #     print("open failed")

    # def dataupdate(self,ss,n):
    #     dataall = ss[6:]
    #     print("检测到传感器数量：",str((n-1)/32))
    #     for i in range(int((n-1)/32)):
    #         data=dataall[:32]
    #         dataall=dataall[32:]
    #         print (data)
    #         ID=data[:8]
    #         value=data[8:12]
    #         value=binascii.b2a_hex(value).decode('utf-8')
    #         print (ID)
    #         # ID=b'\x5A\xA5'
    #         print ("传感器ID：",binascii.b2a_hex(ID).decode('utf-8'))
    #         value = struct.unpack('<f', binascii.unhexlify(value))[0]
    #         print("传感器数值：",str(value) )

    def handle(self):

        self.serial.write(b'\xAA\xAA\xFF\xFF\x01\x6E\xBE\x59\x55\x55\x55')
        data = self.serial.readall()
        print(data)
        self.serial.close()
        ss = data
        sensor_list={}
        sensor_value={}

        print(ss[4:5])
        print(len(ss))
        n = int.from_bytes(ss[4:5], byteorder='little', signed=False)
        print(n)
        ID_r='-1'
        va_r="-1"
        if n>1:
            # self.dataupdate(ss,n)
            dataall = ss[6:]
            print("检测到传感器数量：", str((n - 1) / 32))
            for i in range(int((n - 1) / 32)):
                data = dataall[:32]
                dataall = dataall[32:]
                print(data)
                ID = data[:8]
                value = data[8:12]
                value = binascii.b2a_hex(value).decode('utf-8')
                print(ID)

                print(ID[::-1])
                model_r=self.modelnum(ID)
                # # ID=b'\x5A\xA5'
                #

                # ID=b'\x5A\xA5'

                # ID_r = binascii.b2a_hex(ID)
                # b = bin(int(ID_r, 16))[2:]

                ID_r=binascii.b2a_hex(ID[::-1]).decode('utf-8')
                # print (ID_r[::-1])
                print("传感器ID：", ID_r)
                value = struct.unpack('<f', binascii.unhexlify(value))[0]
                print("传感器数值：", str(value))
                va_r=str(value)
                sensor_value={str(ID_r):[str(va_r),str(model_r),"57%","正常"]}
                sensor_list.update(sensor_value)

        return sensor_list

    def modelnum(self,strvalue):
        ID_m = binascii.b2a_hex(strvalue[::-1])
        # # ID_r=ID.hex()
        # # print(encode(ID_r))
        print(ID_m.decode('UTF-8'))

        b = bin(int(ID_m, 16))[2:]
        print(b)
        # b=b[2:]
        # result = int(ID, base=2)
        # print(hex(result))
        print(b[4:20])

        result = int(b[4:20], base=2)
        print(hex(result))

        if str(hex(result))=='0x5':
            result="温度传感器"
            print ("温度传感器")
        elif str(hex(result)) == '0x6':
            result = "温度传感器"
            print("温度传感器")
        elif str(hex(result))=='0x60':
            result="气压传感器"
            print ("气压传感器")
        elif str(hex(result))=='0x66':
            result="振动传感器Y轴"
            print ("振动传感器Y轴")
        elif str(hex(result))=='0x42':
            result="水位传感器"
            print ("水位传感器")
        elif str(hex(result))=='0x65':
            result="振动传感器X轴"
            print ("振动传感器X轴")
        return result










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
    # ss=data
    # # ss= b'\xaa\xaaB\xc4\xc1\xee\xef\xb8qA(\x03P\x00\xf4\xfd\xd4;\x14\x01\x01\x04#\xb8\x0b \xc7\x02\x00\x00[\x00\x00\x00\x00\x00\x00\x00\xef\xb8qA0\x03P\x00\n\xd7\xa3<\x14\x01\x01\x04"\x90e \xc7\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00\xef\xb8qA8\x03P\x00?5~\xbf\x14\x01\x01\x04 \x88\x90 \xc7\x02\x00\x00W\x00\x00\x00\x00\x00\x00\x00\xd4SqA(\x00P\x00\x00\x00\xc0A\x14\x01\x01\x04#(#\x00\xc6\x02\x00\x00P\x00\x00\x00\x00\x00\x00\x00\xfbEqA(\x00P\x00\x00\x00\xb8A\x14\x01\x01\x04#\xe0\xab\x00\xc6\x02\x00\x00T\x00\x00\x00\x00\x00\x00\x00\x19\xa8qA(\x00P\x00\x00\x00\xb0A\x14\x01\x01\x04#\xd8Y \xca\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00$\xa0UU'
    # # ss=b'\xaa\xaaB\xc4A\xee\xfbEqA(\x00P\x00\x00\x00\xb8A\x14\x01\x01\x05\x08X\x1b\x00\xc6\x02\x00\x00Q\x00\x00\x00\x00\x00\x00\x00\x19\xa8qA\x00\x03P\x00\x00J\xc7G\x14\x01\x01\x05\x05(# \xca\x02\x00\x00X\x00\x00\x00\x00\x00\x00\x00\x9a\xfbUU'
    #
    #
    # # data = '00 00 AC 41'
    # # fdata = struct.unpack('<f', binascii.unhexlify(data.replace(' ', '')))[0]
    # # print(fdata)
    # #
    # # data1 = '0000AC41'
    # # fdata = struct.unpack('<f', binascii.unhexlify(data1))[0]
    # # print("变换",str(fdata))
    #
    # # a=b'\xaaB'
    # # a = struct.pack("2I", 12, 34)
    # # print (a)
    #
    # # b = struct.unpack("2I", a)
    # #
    # # print (b)
    #
    # print (ss[4:5])
    # print (len(ss))
    # n = int.from_bytes(ss[4:5], byteorder='little', signed=False)
    # print (n)
    # if n>1:
    #     dataall = ss[6:]
    #     print("检测到传感器数量：",str((n-1)/32))
    #     for i in range(int((n-1)/32)):
    #         data=dataall[:32]
    #         dataall=dataall[32:]
    #         print (data)
    #         ID=data[:8]
    #         value=data[8:12]
    #         value=binascii.b2a_hex(value).decode('utf-8')
    #         print (ID)
    #         # ID=b'\x5A\xA5'
    #         print ("传感器ID：",binascii.b2a_hex(ID).decode('utf-8'))
    #         value = struct.unpack('<f', binascii.unhexlify(value))[0]
    #         print("传感器数值：",str(value) )
            # str1 = ID.decode('UTF-8')


            # print("str1: ", str1)
    g=gw_model()
    sensor_list=g.handle()
    # ID='0000000000000101'
    # result=int(ID,base=2)
    # print(hex(result))
    # ID=b'\x5A\x00'
    # print(ID[::-1])
    # # # ID=b'\x5A\xA5'
    # #
    # ID_r = binascii.b2a_hex(ID[::-1])
    # # # ID_r=ID.hex()
    # print(ID_r.decode('UTF-8'))
    # b = bin(int(ID_r, 16))[2:]
    # print (b)


