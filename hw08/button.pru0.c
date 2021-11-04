#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

#define pin1 0x1<<5
#define pin2 0x1<<3

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {

	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	while(1) {

		if(!(__R31 & pin2)){
			__R30 |= pin1;
		}
		else{
			__R30 &= ~pin1;
		}
	}

}
