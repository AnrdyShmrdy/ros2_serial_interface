const int baud_r = 9600;
const int fPinNo = 2; //first pin number
const int lPinNo = 13; //last pin number
const int ENA = 9;
const int IN1 = 7;
const int IN2 = 6;
const int IN3 = 5;
const int IN4 = 4;
const int ENB = 3;
const char move_forward = 'w';
const char move_backward = 's';
const char turn_left = 'a';
const char turn_right = 'd';
const char stop = 'x';

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

  if (command == move_forward) //move-forward
  {
    Serial.println("move-forward");
    moveForward();
  }
  else if (command == move_backward) //move-backward
  {
    Serial.println("move-backward");
    moveBackward();
  }
  else if (command == turn_left) //turn-left
  {
    Serial.println("turn-left");
    turnLeft();

  }
  else if (command == turn_right) //turn-right
  {
    Serial.println("turn-right");
    turnRight();

  }
  else if (command == stop) //stop
  {
    Serial.println("stop");
    stopMoving();
  }
}

void loop() 
{
  // put your main code here, to run repeatedly:
  // Serial Communication Goes Here
  char buffer[1];  
    if(Serial.available()){
      Serial.readBytesUntil(',', buffer,1);
      runCommand(buffer[0]);
    }
    //motorTest(DriveMotor1, 2000);
  
}
