import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/tty.usbserial-FTDWJMWC',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    
)

if ser.isOpen():
    print("Connection established. Reading...")

try:
    while True:
        print(ser.readline().decode())

except KeyboardInterrupt:
    print("closing connection...stopping the unit.")
    ser.write('#'.encode())
    ser.close()
    print("Close.")
