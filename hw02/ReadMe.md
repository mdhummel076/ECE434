This is a gpio and keyboard controlled in-terminal etch-a-sketch, along with an analysis of gpio timing on the beaglebone

**Measuring a gpio pin on an Oscilloscope

1. 0-250mV
2. 240ms / 4.17 Hz
3. Not very close, 140ms off
4. There is a lot of overhead in linux that messes with the timing
5. 19%
6. 
| input | 0.1   | 0.05  | 0.01 | 0.005 | 0.001 | 0.0001 |
|:-----:|:-----:|:-----:|:----:|------:|:-----:|:------:|
|period | 240ms | 140ms | 58ms | 50ms  | 42ms  | 40ms   |
|% CPU  | 19%   | 31%   | 69%  | 83%   | 96%   | 100%   |
7. The period is pretty unstable, every 15th or so is wrong
8. Using vi causes the period to dissolve completely
9. Yes, down to 38ms
10. Yes again, down to 30ms
11. 30ms is the shortest

*Python

1. 160us, 6.3kHz
2. 100%
3. 
| Method | shell  | Python |
|:------:|:------:|:------:|
|period  | 30ms   | 160us  |
|% CPU   | 100%   | 100%   |

*C

1. 130us, 7.7kHz
2. 100%
3. 
| Method | shell  | Python | C      |
|:------:|:------:|:------:|:------:|
|period  | 30ms   | 160us  | 130us  |
|% CPU   | 100%   | 100%   | 100%   |

**gpiod

| Method | C      | Python |
|:------:|:------:|:------:|
| 1 bit  | 290kHz | 56kHz  |
| 2 bits | 270kHz | 54kHz  |

**Security

WIP
