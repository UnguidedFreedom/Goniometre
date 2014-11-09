#include <Wire.h>

int address = 0b1000000;

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  while (! Serial) ;
}

void loop()
{    
    Wire.beginTransmission(address);
    Wire.write(0xFE);
    Wire.endTransmission();
    
    Wire.requestFrom(address, 1);
    unsigned char fe = Wire.read();
    
    Wire.beginTransmission(address);
    Wire.write(0xFF);
    Wire.endTransmission();
    
    Wire.requestFrom(address, 1);
    unsigned char ff = Wire.read();
    
    Serial.println((float)((unsigned int)(ff<<6)+(fe&0x3F))*360./(1<<14));
    
    delay(500);
}
