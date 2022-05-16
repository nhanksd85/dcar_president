import serial.tools.list_ports
import time

print("DCAR PRESIDENT")

uart_port = ""
if len(uart_port) > 0:
    ser = serial.Serial(port=uart_port, baudrate=115200)
    
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
while True:

    if len(uart_port) >  0:
        readSerial()
    time.sleep(0.1)