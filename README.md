# TempOnSevenSegment
Show cpu temperature on a seven segment display.

This project has the scope to show the current CPU temperature on an Arduino.

PC: it hosts a simple web page that has just the temperature value inside;
Raspberry PI: read that web page, gets that temperature and sends it using I2C to an Arduino (if the web page is not present it sends 0);
Arduino: receves that temperature value and it displays it on two seven segment displays (common cathode) using an MAX7219 IC;
The schematic to follow can be found in the schematics folder, it was made using KiCAD, there is also an image in that folder.
