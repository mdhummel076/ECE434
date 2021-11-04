#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define pin 0x1<<5

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1) {
		__R30 |= pin;	// The the pin on

		//__delay_cycles(1);    	// Wait 1 millisecond

		__R30 &= ~pin;

		//__delay_cycles(1); 

	}
	//__halt();
}

// Turns off triggers
//#pragma DATA_SECTION(init_pins, ".init_pins")
//#pragma RETAIN(init_pins)
//const char init_pins[] =  
//	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
//	"\0\0";
