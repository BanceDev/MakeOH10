//ToggleLight
#define RED 4
#define YELLOW 5
#define GREEN 2
#define BLUE 3
#define BUZZER 6
#define BUTTON1 7
#define BUTTON2 8
#define BUTTON3 9
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
}
void loop() {
if (digitalRead(BUTTON1)) {
digitalWrite(GREEN, HIGH);
} else {
digitalWrite(GREEN, LOW);
}
}
