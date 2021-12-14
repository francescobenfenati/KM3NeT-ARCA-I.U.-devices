import pyvisa
import time
from pyvisa.constants import StopBits, Parity

rm=pyvisa.ResourceManager()
print(rm.list_resources())


#rs-232 interface
try:
    try:
        minisvs = rm.open_resource('ASRL/dev/cu.usbserial-FTDWJMWC::INSTR',baud_rate=9600, data_bits=8, parity=Parity.none, stop_bits=StopBits.one,timeout=None)
        print("Connection established.")
    except Exception as e:
        print("e")

    while True :
        # get keyboard input
        raw_input = input(">> ")
        if raw_input == 'exit':
            minisvs.close()
            exit()
        elif raw_input == '':
            continue
        elif raw_input == "#":
            minisvs.write(raw_input)
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            if minisvs.bytes_in_buffer > 0:
                #print("flushing")
                #minisvs.flush()
                print("Remaining bytes in buffer: ",minisvs.bytes_in_buffer)
                print("Reading...")
                #read() reads until end of line character encountered. After '#' command, the device sends a '>', with no eol character so that the read() would get stuck in the while loop.
                while minisvs.bytes_in_buffer > 1:
                    print(minisvs.read())
                    print(minisvs.bytes_in_buffer)
                print("Stopping the unit.")
            
        else:
            # send the character to the device
            minisvs.write(raw_input)
            time.sleep(1)
            try:
                while True:
                    print(minisvs.read())
            except KeyboardInterrupt:
                pass

except KeyboardInterrupt:
    print("closing connection...")
    minisvs.close()
    print("Close.")
