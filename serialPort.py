import serial
import time

# opening serial port
ser = serial.Serial('/dev/ttyUSB0')

# removing any pending data on it
ser.flush()

# asking for data on the SD card
ser.write('r'.encode('utf-8'))

# waiting for data to be available
while ser.inWaiting() == 0:
    pass

data = []

while ser.inWaiting() > 0:
    try:
    	# the [:-2] is to remove "\r\n"
        line = ser.readline()[:-2].decode()
        if not line:
            break
        if line == "BEGIN": # new exercise
            data.append([])
        else :
            data[-1].append(eval(line))

        # allows the Arduino to send enough data
        time.sleep(0.01)

    except SyntaxError:
        # when doing eval() on the end of file string
        break

print(data)

ser.write('d'.encode('utf-8')) # erase SD card when done

ser.close()