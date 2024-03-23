#define YELLOW 5
#define RED 4
#define GREEN 3
#define BLUE 2
#define BUZZER 6
#define b1 7
#define b2 8
#define b3 9

// LCD Library
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(BUZZER,OUTPUT);

  //button setup
  pinMode(b1, INPUT_PULLUP);  
  pinMode(b2, INPUT_PULLUP);
  pinMode(b3, INPUT_PULLUP);  

  //LCD Setup
  lcd.init(); // Initialize the LCD I2C display
  lcd.backlight();
  lcd.setCursor(3, 0);          // move cursor to   (3, 0)
  lcd.print("Hello World");        // print message at (3, 0)
  lcd.setCursor(0, 1);          // move cursor to   (0, 1)
  lcd.print("Clymer Fanclub"); // print message at (0, 1)
}

void loop() {
  // LED Output Tests
  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);

  // Buzzer Tests (bad sound)
  digitalWrite(BUZZER, HIGH);
  //digitalWrite(RED, HIGH);
  //digitalWrite(YELLOW, HIGH);
  //digitalWrite(GREEN, HIGH);
  //digitalWrite(BLUE, HIGH);
  //delay(15000);
  //digitalWrite(BUZZER, LOW);

    //add another 500 milliseconds of silence
  if (digitalRead(b1) == LOW)
  {
    digitalWrite(RED, HIGH);
  }
  if (digitalRead(b2) == LOW)
  {
    digitalWrite(GREEN, HIGH);
  }
  if (digitalRead(b3) == LOW)
  {
    digitalWrite(BLUE, HIGH);
  }
  //delay(200);
}
