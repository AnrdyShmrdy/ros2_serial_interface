//Make ten Motors
//index 0 = Dir, index 1 = Step, index 2 = Enable

int DriveMotor1[] = {50,11,15};  // back left wheel
int DriveMotor2[] = {46,9,17};   // front left wheel
int DriveMotor3[] = {40,6,66};  //back right wheel
int DriveMotor4[] = {36,4,69};   //front right wheel

int ArmMotor1[] = {52,12,14};
int ArmMotor2[] = {42,8,18};
int ArmMotor3[] = {44,7,19};
int ArmMotor4[] = {48,10,16};
int ArmMotor5[] = {38,5,67};
int ArmMotor6[] = {34,3,69};

//Serial: Input data comes from USB CABLE; Read Serial for pulse calls

void setup() {
  // put your setup code here, to run once:
  //Up the speed of the internal timer
  TCCR1A = 0b00000011; // 10bit
  TCCR1B = 0b00001001; // x1 fast pwm
  //For loop to determine all Motor Pin Connections
  for(int i = 0; i<3; i++)
  {
  pinMode(DriveMotor1[i], OUTPUT);
  pinMode(DriveMotor2[i],OUTPUT);
  pinMode(DriveMotor3[i],OUTPUT);
  pinMode(DriveMotor4[i],OUTPUT); 
  pinMode(ArmMotor1[i],OUTPUT);
  pinMode(ArmMotor2[i],OUTPUT);
  pinMode(ArmMotor3[i],OUTPUT);
  pinMode(ArmMotor4[i],OUTPUT);
  pinMode(ArmMotor5[i],OUTPUT);
  pinMode(ArmMotor6[i],OUTPUT);
  //Set all Motors to No Output
  digitalWrite(DriveMotor1[i],LOW);
  digitalWrite(DriveMotor2[i],LOW);
  digitalWrite(DriveMotor3[i],LOW);
  digitalWrite(DriveMotor4[i],LOW);
  digitalWrite(ArmMotor1[i],LOW);
  digitalWrite(ArmMotor2[i],LOW);
  digitalWrite(ArmMotor3[i],LOW);
  digitalWrite(ArmMotor4[i],LOW);
  digitalWrite(ArmMotor5[i],LOW);
  digitalWrite(ArmMotor6[i],LOW);
  }
  //Start up Serial Communication
  Serial.begin(9600);
  
}

void Start(int motor[], bool enab, bool direc)
{
  if(enab == 1){
    digitalWrite(motor[2],LOW); //For some reason, setting to LOW enables
    if(direc == 1)
    {
      digitalWrite(motor[0],LOW);
    }
    if(direc == 0)
    {
      digitalWrite(motor[0],HIGH);
    }

    analogWrite(motor[1], 127);
  }
}


//For some reason this modification to Start caused motor to start stuttering. 
//void Start(int motor[], bool direc)
//{
//  digitalWrite(motor[0],LOW); 
//  if(direc == 1)
//  {
//    digitalWrite(motor[0],LOW);
//  }
//  if(direc == 0)
//  {
//    digitalWrite(motor[0],HIGH);
//  }
//
//  analogWrite(motor[2], 127);
//}

void Stop(int motor[])
{
  digitalWrite(motor[2],HIGH);
  digitalWrite(motor[0],LOW);
  analogWrite(motor[1], 0);
}

/* Movement Functions:
 * Imagine a top-down view of the rover, with the front of it facing north
 * My assumption is that the motors are numbered going from left-to-right and front-to-back
 * If assumption is incorrect the values can easily be changed later
 * #1=Front-left wheel motor
 * #2=Front-right wheel motor
 * #3=Back-left wheel motor
 * #4=Back-right wheel motor
 * 
 * NEW ASSIGNMENT OF MOTORS:
 * #1= Back-left wheel
 * #2= Front-left wheel
 * #3= Back-right wheel
 * #4= Front-right wheel
*/

void moveForward(){
  Start(DriveMotor2, 1, 1);
  Start(DriveMotor4, 1, 1);
  Start(DriveMotor1, 1, 1);
  Start(DriveMotor3, 1, 1);
}
void moveBackward(){
  Start(DriveMotor2, 1, 0);
  Start(DriveMotor4, 1, 0);
  Start(DriveMotor1, 1, 0);
  Start(DriveMotor3, 1, 0);
}
void turnLeft(){
  Start(DriveMotor2, 1, 0);
  Start(DriveMotor4, 1, 1);
  Start(DriveMotor1, 1, 0);
  Start(DriveMotor3, 1, 1);
}
void turnRight(){
  Start(DriveMotor2, 1, 1);
  Start(DriveMotor4, 1, 0);
  Start(DriveMotor1, 1, 1);
  Start(DriveMotor3, 1, 0);
}
void stopMoving(){
  Stop(DriveMotor2);
  Stop(DriveMotor4);
  Stop(DriveMotor1);
  Stop(DriveMotor3);
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

void motorTest(int motor[], int ms_delay){
  digitalWrite(motor[2],LOW); //Motor is Enabled
  digitalWrite(motor[0],HIGH); //Motor direction set HIGH
  analogWrite(motor[1], 127); //Motor step amount set to 127
  delay(ms_delay); //delay
  digitalWrite(motor[2],HIGH); //Motor is Disabled
  digitalWrite(motor[0],LOW); // Motor direction set LOW
  analogWrite(motor[1], 0); //Motor step amount set to 0
  delay(ms_delay); //delay
}

void loop() 
{
  // put your main code here, to run repeatedly:
  // Serial Communication Goes Here
    if(Serial.available()){
      //char command = Serial.read();
      //runCommand(command);
    }
    motorTest(DriveMotor1, 2000);
  
}
