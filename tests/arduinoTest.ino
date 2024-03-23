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
  digitalWrite(RED, HIGH);
  digitalWrite(YELLOW, HIGH);
  digitalWrite(GREEN, HIGH);
  digitalWrite(BLUE, HIGH);

  // Buzzer Tests (bad sound)
  //tone(BUZZER ,400,300);

    //add another 500 milliseconds of silence

    //delay(1000);
}
