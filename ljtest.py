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


def test_wn():
    """
    """
    #print("Initiating White Noise")
    value = 2.5
    pin_name = 'DAC0'
    # Write to Register pin name
    ljm.eWriteName(handle, pin_name, value)
    # Read the Register pin Name
    #print('%s Voltage: %s' % (pin_name, ljm.eReadName(handle, pin_name)))
    time.sleep(0.04) # waite 40 ms
    value = 1
    pin_name = 'DAC0'
    # Write to Register pin name
    ljm.eWriteName(handle, pin_name, value)
    # Read the Register pin Name
    #print('%s Voltage: %s' % (pin_name, ljm.eReadName(handle, pin_name)))

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

def write_Parallel(value):
    """
    """
    if (value > 255):
        print('value given is too hight')
        return
    if (value < 0):
        print('value given is too low')
        
    binary_num = format(value, "08b")
    print(binary_num)
    for bit in range(8):
        print(bit)
        if
    
    
if __name__ == '__main__':
    write_Parallel(0)
    setPIN('DIO12')
        