#define RED 2
#define YELLOW 3
#define GREEN 4
#define BLUE 5
#define BUZZER 6

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
  digitalWrite(RED, HIGH);
  digitalWrite(YELLOW, HIGH);
  digitalWrite(GREEN, HIGH);
  digitalWrite(BLUE, HIGH);
  delay(15000);
  digitalWrite(BUZZER, LOW);

    //add another 500 milliseconds of silence

  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
  delay(200);
}
