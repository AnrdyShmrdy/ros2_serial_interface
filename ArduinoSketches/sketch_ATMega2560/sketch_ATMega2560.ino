//Make ten Motors
int DriveMotor1[] = {7,3,5}; //index 0 = sleep, index 1 = direction, index 2 = steps
int DriveMotor2[] = {17,13,15}; //index 0 = sleep, index 1 = direction, index 2 = steps
int DriveMotor3[] = {27,23,25}; //index 0 = sleep, index 1 = direction, index 2 = steps
int DriveMotor4[] = {37,33,25};
//Andy: Commented out below line since this variable isn't being used
//int DriveMotorDirectory[] = {DriveMotor1, DriveMotor2, DriveMotor3, DriveMotor4};
int ArmMotor1[] = {47,43,45};
int ArmMotor2[] = {57,53,55};
int ArmMotor3[] = {67,63,65};
int ArmMotor4[] = {77,73,75};
int ArmMotor5[] = {87,83,85};
int ArmMotor6[] = {97,93,95};

//Serial: Input data comes from USB CABLE; Read Serial for pulse calls

void setup() {
  // put your setup code here, to run once:

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
    digitalWrite(motor[0],HIGH); 
    if(direc == 1)
    {
      digitalWrite(motor[1],LOW);
    }
    else
    {
      digitalWrite(motor[1],HIGH);
    }

    analogWrite(motor[2], 127);
  }
  else{
    Stop(motor);
  }
}

void Stop(int motor[])
{
  digitalWrite(motor[0],LOW);
}

void turnMotors(char ch)
{
  /*
  Imagine a top-down view of the rover, with the front of it facing north
  My assumption is that the motors are numbered going from left-to-right and front-to-back
  If assumption is incorrect the values can easily be changed later
  #1=Front-left wheel motor
  #2=Front-right wheel motor
  #3=Back-left wheel motor
  #4=Back-right wheel motor
  */
  if (ch == 'w') //move-forward
  {
    Serial.println("move-forward");
    Start(DriveMotor1, 1, 1);
    Start(DriveMotor2, 1, 1);
    Start(DriveMotor3, 1, 1);
    Start(DriveMotor4, 1, 1);
  }
  else if (ch == 's') //move-backward
  {
    Serial.println("move-backward");
    Start(DriveMotor1, 1, 0);
    Start(DriveMotor2, 1, 0);
    Start(DriveMotor3, 1, 0);
    Start(DriveMotor4, 1, 0);
  }
  else if (ch == 'a') //turn-left
  {
    Serial.println("turn-left");
    Start(DriveMotor1, 1, 0);
    Start(DriveMotor2, 1, 1);
    Start(DriveMotor3, 1, 0);
    Start(DriveMotor4, 1, 1);
  }
  else if (ch == 'd') //turn-right
  {
    Serial.println("turn-right");
    Start(DriveMotor1, 1, 1);
    Start(DriveMotor2, 1, 0);
    Start(DriveMotor3, 1, 1);
    Start(DriveMotor4, 1, 0);
  }
  else if (ch == 'x') //stop
  {
    Serial.println("stop");
    Stop(DriveMotor1);
    Stop(DriveMotor2);
    Stop(DriveMotor3);
    Stop(DriveMotor4);
  }
}

void loop() 
{
  // put your main code here, to run repeatedly:
  // Serial Communication Goes Here
    if(Serial.available()){
      //Andy: Commented out to test alternative way
      // byte MotorCommand[2];
      // Serial.readBytes(MotorCommand, 2); //Captures the first 2 bytes of data sent 
      // // it will send 16 bits: 0000 0000 0000 0000
      // // First Byte (8 bits) determines if the command is sent to Drive motors or Arm motors
      // if(MotorCommand[0] == 0){
      //   // BYTE 1: 0000 0000
      //   //Drive Motor Command

      //   for(int i = 0; i<4; i++){
      //     bool enab = bitRead(MotorCommand[1], i);  //XXXX 0000
      //     bool direc = bitRead(MotorCommand[1], i+4); //0000 XXXX
      //     Start(DriveMotorDirectory[i], enab, direc);
      //   }
      // }
      // else if(MotorCommand[0] == 128){
      //   // BYTE 1: 1000 0000
      //   //Arm Motor Command

      // }
      char ch = Serial.read();
      turnMotors(ch);
    }
    //Start(DriveMotor1,1);
    //delay(500);
    //Stop(DriveMotor1);
  
}
