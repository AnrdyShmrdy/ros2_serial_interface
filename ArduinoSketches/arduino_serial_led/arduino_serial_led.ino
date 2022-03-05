const int Led1 = 3;
const int Led2 = 5;
const int Led3 = 7;
const int Led4 = 9;

void setup() 
{
  pinMode(Led1, OUTPUT);
  pinMode(Led2, OUTPUT);
  pinMode(Led3, OUTPUT);
  pinMode(Led4, OUTPUT);

  Serial.begin(9600);
  while (! Serial); // Wait untilSerial is ready - Leonardo
  Serial.println("Enter 0 to turn off LED and 1 to turn on LED");
}

void loop() 
{
  if (Serial.available())
  {
    char ch = Serial.read();
    if (ch == '0')
    {
      digitalWrite(Led1,LOW);
      digitalWrite(Led2,LOW);
      digitalWrite(Led3,LOW);
      digitalWrite(Led4,LOW);
      delay(10);
      Serial.println("All Leds Turned OFF");
    }    
    if (ch == '1')
    {
      digitalWrite(Led1,HIGH);
      delay(10);
      Serial.println("Led1 Turned ON");
    }
    if (ch == '2')
    {
      digitalWrite(Led2,HIGH);
      delay(10);
      Serial.println("Led2 Turned ON");
    }
    if (ch == '3')
    {
      digitalWrite(Led3,HIGH);
      delay(10);
      Serial.println("Led3 Turned ON");
    }
    if (ch == '4')
    {
      digitalWrite(Led4,HIGH);
      delay(10);
      Serial.println("Led4 Turned ON");
    }
    if (ch == '5')
    {
      digitalWrite(Led1,LOW);
      delay(10);
      Serial.println("Led1 Turned OFF");
    }
    if (ch == '6')
    {
      digitalWrite(Led2,LOW);
      delay(10);
      Serial.println("Led2 Turned OFF");
    }
    if (ch == '7')
    {
      digitalWrite(Led3,LOW);
      delay(10);
      Serial.println("Led3 Turned OFF");
    }
    if (ch == '8')
    {
      digitalWrite(Led4,LOW);
      delay(10);
      Serial.println("Led4 Turned OFF");
    }
    if (ch == '9')
    {
      digitalWrite(Led1,HIGH);
      digitalWrite(Led2,HIGH);
      digitalWrite(Led3,HIGH);
      digitalWrite(Led4,HIGH);
      delay(10);
      Serial.println("All Leds Turned ON");
    }
  }
}
