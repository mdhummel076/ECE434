# Hw 4 #

## Memory Map ##

![image](https://user-images.githubusercontent.com/43393092/135877225-4d137da8-e1cb-454e-aeba-be964ee7a006.png)

### mmap ###

LEDS.py uses mmap to read two buttons and control two leds

ledToggle.py uses mmap to toggle a gpio pin as fast as possible(in python)

The maximum frequency achieved by mmap in python was 92kHz

### Etch-a-sketch ###

etch-a-sketch.py contains an etch-a-sketch program that uses flask and the i2c 8x8 led matrix to play etch-a-sketch from the web server on the led matrix. Demoed in class

app4.py is example code used to make etch-a-sketch.py, and templates contains the html for the web server

### LCD display ###

boris.png, name.png and tada.png are each image file either used as examples or created by me using imagemagick. Each was displayed on the lcd during the in class demo.

# hw04 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Memory map 
|  4/4 | mmap()
|  0/4 | i2c via Kernel  | *Missing*
|  5/5 | Etch-a-Sketch via flask
|  5/5 | LCD display
|      | Extras
| 16/20 | **Total**

*My comments are in italics. --may*

