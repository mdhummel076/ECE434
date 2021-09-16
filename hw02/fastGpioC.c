// Blink pin 60 at AFAP

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "gpio-utils.h"

int main(int argc, char** argv)
{

	char set_value[5]; 
	int toggle = 0;
	int gpio = 60;
	int gpio_fd;
	
	gpio_export(gpio);
	
	//SET DIRECTION
	gpio_set_dir(gpio, "out");
			
	//Run an infinite loop - will require Ctrl-C to exit this program
	while(1)
	{
		toggle = !toggle;
		
		lseek(gpio_fd, 0, 0);

		if (toggle)
			write(gpio_fd, "1", 2);
		else
			write(gpio_fd, "0", 2);
	}

	return 0;
}
