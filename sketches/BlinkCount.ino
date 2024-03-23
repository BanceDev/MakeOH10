//BlinkCount
#define RED 2
#define YELLOW 3
#define GREEN 4
#define BLUE 5
#define BUZZER 6
void setup() {
pinMode(RED, OUTPUT);
pinMode(YELLOW, OUTPUT);
pinMode(GREEN, OUTPUT);
pinMode(BLUE, OUTPUT);
pinMode(BUZZER,OUTPUT);
}
void loop() {
for (int i = 0; i < 10; i++) {
digitalWrite(GREEN, HIGH);
delay(1);
digitalWrite(GREEN, LOW);
delay(1);
}
for (int i = 0; i < 10; i++) {
digitalWrite(RED, HIGH);
delay(1);
digitalWrite(RED, LOW);
delay(1);
}
for (int i = 0; i < 10; i++) {
digitalWrite(BLUE, HIGH);
delay(1);
digitalWrite(BLUE, LOW);
delay(1);
}
}
