import pyvisa
import time
from pyvisa.constants import StopBits, Parity

rm=pyvisa.ResourceManager()
print(rm.list_resources())
#does not show tcpip interface but nonetheless you can connect to it

#usb interface
#agilent=rm.open_resource('USB0::2391::6407::MY50002594::0::INSTR')

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
        if raw_input == '':
            continue
        if raw_input == "#":
        #    raw_input=raw_input.encode()
            minisvs.write(raw_input)
            while True:
                print("flushing")
                minisvs.flush()
        #        if ser.in_waiting > 0:
        #            print("bytes in buffer: ",ser.in_waiting)
        #            print(ser.readline())
        #        else:
        #            print("after giving # command, the buffer is empty: ",ser.in_waiting)
        #            break

        else:
            # send the character to the device
            minisvs.write(raw_input)
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            try:
                while minisvs.bytes_in_buffer > 0:
                    print(minisvs.read())
                    print(minisvs.bytes_in_buffer)
            except KeyboardInterrupt:
                pass

except KeyboardInterrupt:
    print("closing connection...")
    minisvs.close()
    print("Close.")
