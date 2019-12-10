import serial
import struct

class TriggerBox():
    '''
    Author: Yu Pei, 1666424499@qq.com
    Versions:
        v1.0: 2019-12-9,
    '''

    def __init__(self):
        self.portx  = "COM3"
        self.bps    = 115200            # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        self.timex  = 5                 # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        self.ser         = serial.Serial(    # 打开串口，并得到串口对象
            self.portx,
            self.bps,
            timeout=self.timex)

    def OutputEventData(self,data):
        try:
            message = struct.pack("BBBBB", 1,225,1,0,data)
            self.ser.flush()
            self.ser.write(message)     # 向串口写入数据。
            self.ser.flushInput()
            self.ser.flushOutput()
        except Exception as e:
            print("---异常---：", e)
            self.ser.close()

    def __del__(self):
        self.ser.close()


