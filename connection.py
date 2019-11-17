import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14201',9600)

def getLatestStatus():
    status = ser.readline()
    while ser.inWaiting() > 0:
        status = ser.readline()
    return status

# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):
    b = getLatestStatus()           # read a byte string
    string_n = b.decode()           # decode byte string into Unicode  
    string = string_n.rstrip()      # remove \n and \r
    data.append(string)             # add to the end of data list
    print(string)
    time.sleep(0.1)                 # wait (sleep) 0.1 seconds


'''b = ser.readline()
str_rn = b.decode()
str = str_rn.rstrip()
print(str)
ser.close()'''
