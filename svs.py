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

raw_input=1
try:
    while True :
        # get keyboard input
        raw_input = input(">> ")
        if raw_input == 'exit':
            ser.close()
            exit()
        elif raw_input == '':
            continue
        elif raw_input == "#":
            raw_input=raw_input.encode()
            ser.write(raw_input)
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            if ser.in_waiting > 0:
                print("Remaining bytes in buffer: ",ser.in_waiting)
                print("Reading...")
                #print("flushing")
                #ser.reset_input_buffer()
                print(ser.read(ser.in_waiting).decode())
                print("Now the buffer is empty: ",ser.in_waiting,", stopping the unit.")

        else:
            # send the character to the device
            raw_input+='\r\n'
            raw_input=raw_input.encode()
            ser.write(raw_input)      
            time.sleep(1)
            try:
                while True:
                    print(ser.readline().decode())
            except KeyboardInterrupt:
                pass

except KeyboardInterrupt:
    print("closing connection...")
    ser.close()
    print("Close.")
