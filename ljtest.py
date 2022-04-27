#!/usr/bin/env python

# Testing the DB 15/25 Connection


from labjack import ljm
import sys, time
import msvcrt
# Open first found LabJack
try:
    handle = ljm.openS("ANY", "ANY", "ANY")
except:
    print('not labjack plugged int?')
    sys.exit(0)




def test_shock():
    # Pulse Rise every 2ms, since DIGITMER has a limit duration of 2ms
    #print("Initiating Shock")
    for stim in range(20):
        ljm.eWriteName(handle, 'DAC1', 5) # rise up 
        #print('%s Voltage: %s' % ('DAC1', ljm.eReadName(handle, 'DAC1')))
        time.sleep(.002)
        ljm.eWriteName(handle, 'DAC1', 1) # rise down
        #print('%s Voltage: %s' % ('DAC1', ljm.eReadName(handle, 'DAC1')))
        time.sleep(.003)

def setPIN(name):
    ljm.eWriteName(handle, name, 0)
#print("\neReadName result: ")
#print("    %s = %f" % (name, result))


def clear_bits():
    for bit in range(8):
        ljm.eWriteName(handle, 'DIO' + str(bit + 4), 0) 

def test_labjack():
    clear_bits()
    for value in range(256):
        print('writing value: ' + value)
        for bit in range(8):
            ljm.eWriteName(handle, 'DIO' + str(bit + 4), 5) 

            

if __name__ == '__main__':
    test_labjack()