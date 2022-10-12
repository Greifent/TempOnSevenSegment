#include "LedControl.h"
#include <Wire.h>
LedControl lc=LedControl(12,11,10,1);

void setup() {
  lc.shutdown(0,false);
  lc.setIntensity(0,1);
  lc.clearDisplay(0);
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
}

void showValue(int i){
    lc.setDigit(0,1,((int)i/10*10-(int)i/100*100)/10,false);
    lc.setDigit(0,0,i-(int)i/10*10,false);
}

void receiveEvent(int howMany) {
  int value;
  while (Wire.available()) {
    value = Wire.read(); // receive byte as a character
  }
  showValue(value);
}

void loop() {
  // put your main code here, to run repeatedly:

}
