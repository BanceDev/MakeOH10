#define RED 2
#define YELLOW 3
#define GREEN 4
#define BLUE 5
#define BUZZER 6

void setup() {
  // put your setup code here, to run once:
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(BUZZER,OUTPUT);
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
  delay(5000);
  digitalWrite(BUZZER, LOW);

    //add another 500 milliseconds of silence

  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
  delay(1000);
}
