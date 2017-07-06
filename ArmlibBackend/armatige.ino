#include <Servo.h>
Servo turn;
Servo exte;
Servo grip;
Servo nodd;
int value;

void setup (){
  Serial.begin(9600);
  Serial.flush();
  digitalWrite (13, HIGH);      //turn on debugging LED
  turn.attach(3);
  exte.attach(5);
  grip.attach(6);
  nodd.attach(9);
  /*turn.write(0); 
   exte.write(0);
   grip.write(0);
   nodd.write(0);*/
   delay(1000);
}

void loop (){
 String servo = Serial.readStringUntil(':');
if(servo != ""){
  Serial.println("Got here!");
  //here you could check the servo number
  String pos = Serial.readStringUntil(';');
  int int_pos=pos.toInt();
  if (servo=="youarm") {
   
   turn.write(0); 
   exte.write(0);
   grip.write(0);
   nodd.write(0);
   delay(1000);
   Serial.println("MeArm!");
  }
  else if (servo=="turn") {
    value = round(map(int_pos,0,1000,0,180));
    turn.write(value);
    delay(1000);
    Serial.println("Done!");
  }
  else if (servo=="exte") {
    value = round(map(int_pos,0,1000,0,65));
    exte.write(value);
    delay(1000);
    Serial.println("Done!");
  }
  else if (servo=="grip") {
    value = round(map(int_pos,0,1000,0,120));
    grip.write(value);
    delay(1000);
    Serial.println("Done!");
  }
  else if (servo=="nodd") {
    value = round(map(int_pos,0,1000,0,120));
    nodd.write(value);
    delay(1000);
    Serial.println("Done!");
  }
  else {
   Serial.println("INVALID COMMAND!"); 
  }
  
  
}
 
}
