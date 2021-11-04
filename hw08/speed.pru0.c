#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define pin 0x1<<17

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	uint32_t *gpio1 = (uint32_t *)GPIO1;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1) {
		gpio1[GPIO_SETDATAOUT]   = pin;	// The the USR3 LED on

		__delay_cycles(0);    	// Wait 1/2 second

		gpio1[GPIO_CLEARDATAOUT] = pin;

		__delay_cycles(0); //500000000/5

	}
}

// Turns off triggers
//#pragma DATA_SECTION(init_pins, ".init_pins")
//#pragma RETAIN(init_pins)
//const char init_pins[] =  
//	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
//	"\0\0";
