const int baud_r = 9600;
const int fPinNo = 2; //first pin number
const int lPinNo = 13; //last pin number
const int ENA = 9;
const int IN1 = 7;
const int IN2 = 6;
const int IN3 = 5;
const int IN4 = 4;
const int ENB = 3;
const int pwm_val = 140;
int DCMotor1[] = {IN1,IN2, ENA};
int DCMotor2[] = {IN3,IN4, ENB};  

//Serial: Input data comes from USB CABLE; Read Serial for pulse calls

void setup() 
{
  for(int i=fPinNo; i <=lPinNo; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(baud_r);
}

void Start(int motor[], bool pin1, bool pin2, int pwm_val)
{
  pin1 ? digitalWrite(motor[0], HIGH) : digitalWrite(motor[0], LOW);
  pin2 ? digitalWrite(motor[1], HIGH) : digitalWrite(motor[1], LOW);
  analogWrite(motor[2], pwm_val);
}
void Stop(int motor[])
{
  digitalWrite(motor[0], 0);
  digitalWrite(motor[1], 0);
  analogWrite(motor[2], 0);
}

void moveForward(){
  Start(DCMotor1, 1, 0, pwm_val);
  Start(DCMotor2, 1, 0, pwm_val);
}
void moveBackward(){
  Start(DCMotor1, 0, 1, pwm_val);
  Start(DCMotor2, 0, 1, pwm_val);
}
void turnLeft(){
  Start(DCMotor1, 1, 0, 195);
  Start(DCMotor2, 0, 1, 195);
}
void turnRight(){
  Start(DCMotor1, 0, 1, 195);
  Start(DCMotor2, 1, 0, 195);
}
void stopMoving(){
  Stop(DCMotor1);
  Stop(DCMotor2);
}
void runCommand(char command)
{

  if (command == 'w') //move-forward
  {
    Serial.println("move-forward");
    moveForward();
  }
  else if (command == 's') //move-backward
  {
    Serial.println("move-backward");
    moveBackward();
  }
  else if (command == 'a') //turn-left
  {
    Serial.println("turn-left");
    turnLeft();

  }
  else if (command == 'd') //turn-right
  {
    Serial.println("turn-right");
    turnRight();

  }
  else if (command == 'x') //stop
  {
    Serial.println("stop");
    stopMoving();
  }
}

void loop() 
{
  // put your main code here, to run repeatedly:
  // Serial Communication Goes Here
    if(Serial.available()){
      char command = Serial.read();
      runCommand(command);
    }
    //motorTest(DriveMotor1, 2000);
  
}
