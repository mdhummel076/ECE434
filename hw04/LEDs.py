#!/usr/bin/env python3
# From: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
from mmap import mmap
import time, struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138

button1 = 1<<28
button2 = 1<<19

led1 = 1<<17
led2 = 1<<18

# Next we need to make the mmap, using the desired size and offset:
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

# The mmap is addressed byte by byte, so we can't just set a single bit. 
# The easiest thing to do is grab the whole 4-byte register:
packed_reg = mem[GPIO_OE:GPIO_OE+4]

# We now have 32 bits packed into a string, so to do any sort of bitwise operations with it we must unpack it:
# The 'L' tells struct.unpack() to unpack the string into an unsigned long, 
# which will give us the full 32-bit register. The '<' tells it that the 
# string is packed little-endian, or least-significant byte first. 
# The BeagleBone's memory is little-endian, so if we tell this to struct.unpack() 
# it will return the 32 bits in the order they are shown in the reference manual register maps.
reg_status = struct.unpack("<L", packed_reg)[0]

# We now have the 32-bit integer value of the register, so we can configure 
# the LED as an output by clearing its bit:
reg_status &= ~(led1 | led2)
reg_status |= (button1 | button2)

# Now all that's left to do is to pack it little-endian back into a string and update the mmap:

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

# Now that we know the pin is configured as an output, it's time to get blinking. 
# We could use the GPIO_DATAOUT register to do this, 
# but we would want to preserve the state of all the other bits in it, 
# so we would need to do the same process of unpacking, manipulating then repacking. 
# That's what the SETDATAOUT and CLEARDATAOUT registers are for. 
# Writes to them affect only the pins whose bits are set to 1, making the next step much easier:
try:
  while(True):
    buttons = mem[GPIO_DATAIN:GPIO_DATAIN+4]
    buttonsVal = struct.unpack("<L", buttons)[0]
    
    button1Val = (buttonsVal >> 28) & 1
    button2Val = (buttonsVal >> 19) & 1
    
    print("Button1: "+str(button1Val)+" Button2: "+str(button2Val))
    
    if(bool(button1Val) and bool(button2Val)):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", led1 | led2)
    elif(button1Val):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", led1)
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", led2)
    elif(button2Val):
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", led2)
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", led1)
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", led1 | led2)

    time.sleep(0.1)

except KeyboardInterrupt:
  mem.close()
