#define led_vermelha 9
#define led_amarela  8
#define led_verde    7

#define btn_a        4
#define btn_b        3

#define pot          A0 

void setup() {
  // put your setup code here, to run once:
  pinMode(led_vermelha, OUTPUT);
  pinMode(led_amarela,  OUTPUT);
  pinMode(led_verde,    OUTPUT);

  pinMode(btn_a, INPUT_PULLUP);
  pinMode(btn_b, INPUT_PULLUP);
  
  pinMode(pot, INPUT); 

  Serial.begin(9600);
  Serial.println("Serial listening");
}

void envia_btnA(){ // PULLUP -> HIGH => 0
  if(digitalRead(btn_a) == HIGH) Serial.println("b0");
  else Serial.println("b1");
}
void envia_btnB(){ // PULLUP -> HIGH => 0
  if(digitalRead(btn_b) == HIGH) Serial.println("B0");
  else Serial.println("B1");
}
void envia_pot(){
  int val = analogRead(pot);
  Serial.print("P");
  Serial.println(val);
}

void processaSerial(){
  if (Serial.available() > 0){
    int a = Serial.read();
    
    if(a == 'r') digitalWrite(led_vermelha, LOW);
    if(a == 'R') digitalWrite(led_vermelha, HIGH);

    if(a == 'g') digitalWrite(led_verde, LOW);
    if(a == 'G') digitalWrite(led_verde, HIGH);
    
    if(a == 'y') digitalWrite(led_amarela, LOW);
    if(a == 'Y') digitalWrite(led_amarela, HIGH);

    if(a == 'b') envia_btnA();
    if(a == 'B') envia_btnB();
    if(a == 'p' || a == 'P') envia_pot();
    
    if(a == 'n' || a == 'N') delay(100);
  }
}

int potReportTimeout = 0;
void processaBroadcast(){
  if(potReportTimeout++ < 10) return;

  potReportTimeout=0;
  envia_pot();
}
void loop() {
  processaSerial();
  //processaBroadcast();
  delay(100);
}

