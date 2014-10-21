#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Goniometre");
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  for(int i=0; i<180; i++)
  {
    lcd.setCursor(0, 1);
    lcd.print(i);
    lcd.print("\262   ");
    delay(200);
  }
  for(int i=180; i>0; i--)  
  {
    lcd.setCursor(0, 1);
    lcd.print(i);
    lcd.print("\262             ");
    delay(200);
  }
}
