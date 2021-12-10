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
    print("Connection established.")
    print('Enter your commands below.\r\nInsert "exit" to leave the application. Press ctrl-c to interrupt polling.')

#    while True:
#        time.sleep(1)
#        print("bytes in buffer when just open: ",ser.in_waiting)
#        print("flushing...",ser.reset_input_buffer())
#        print("reading...",ser.read(76).decode())

raw_input=1
try:
    while True :
        # get keyboard input
        raw_input = input(">> ")
        if raw_input == 'exit':
            ser.close()
            exit()
        if raw_input == '':
            continue
        if raw_input == "#":
            raw_input=raw_input.encode()
            ser.write(raw_input)
        else:
            # send the character to the device
            if raw_input != "#":
                raw_input+='\r\n'
            raw_input=raw_input.encode()
            ser.write(raw_input)

except KeyboardInterrupt:
    print("closing connection...stopping the unit.")
    ser.write('#'.encode())
    ser.close()
    print("Close.")
