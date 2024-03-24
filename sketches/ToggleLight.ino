//ToggleLight
#define RED 2
#define YELLOW 3
#define GREEN 5
#define BLUE 4
#define BUZZER 6
#define BUTTON1 7
#define BUTTON2 8
#define BUTTON3 9
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup() {
pinMode(RED, OUTPUT);
pinMode(YELLOW, OUTPUT);
pinMode(GREEN, OUTPUT);
pinMode(BLUE, OUTPUT);
pinMode(BUZZER, OUTPUT);
pinMode(BUTTON1, INPUT_PULLUP);
pinMode(BUTTON2, INPUT_PULLUP);
pinMode(BUTTON3, INPUT_PULLUP);
digitalWrite(BUZZER, HIGH);
lcd.init();
lcd.backlight();
lcd.setCursor(0, 0);
}
void loop() {
lcd.setCursor(0,0);
lcd.print("Hello Make Oh10!");
if (digitalRead(BUTTON1) == LOW) {
digitalWrite(GREEN, HIGH);
digitalWrite(RED, LOW);
digitalWrite(BLUE, LOW);
} else if (digitalRead(BUTTON2) == LOW) {
digitalWrite(GREEN, LOW);
digitalWrite(RED, HIGH);
digitalWrite(BLUE, LOW);
} else if (digitalRead(BUTTON3) == LOW) {
digitalWrite(GREEN, LOW);
digitalWrite(RED, LOW);
digitalWrite(BLUE, HIGH);
}
}
