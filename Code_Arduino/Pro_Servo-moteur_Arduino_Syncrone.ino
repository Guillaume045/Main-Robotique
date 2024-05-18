//Code pour piloté 5 servo moteur via des bouton

#include <Servo.h>
// 1
int bouton1 = 2;
int etatbouton1 = 0;
Servo servo_1;
// 2
int bouton2 = 3;
int etatbouton2 = 0;
Servo servo_2;
// 3
int bouton3 = 4;
int etatbouton3 = 0;
Servo servo_3;
// 4
int bouton4 = 5;
int etatbouton4 = 0;
Servo servo_4;
// 5
int bouton5 = 6;
int etatbouton5 = 0;
Servo servo_5;

void setup()
{
  Serial.begin (9600);
  pinMode (bouton1, INPUT);
  servo_1.attach(12);
  
  pinMode (bouton2, INPUT);
  servo_2.attach(11);
  
  pinMode (bouton3, INPUT);
  servo_3.attach(10);
  
  pinMode (bouton4, INPUT);
  servo_4.attach(9);
  
  pinMode (bouton5, INPUT);
  servo_5.attach(8);
}

void loop()
{
  etatbouton1 = digitalRead(bouton1);
  
  if (etatbouton1 == LOW) {
    servo_1.write(0);
    Serial.println(etatbouton1);
    delay(10);
  }
  else {
    servo_1.write(180);
    Serial.println(etatbouton1);
    delay(10);
  }
  
  etatbouton2 = digitalRead(bouton2);
  
  if (etatbouton2 == LOW) {
    servo_2.write(0);
    Serial.println(etatbouton2);
    delay(10);
  }
  else {
    servo_2.write(180);
    Serial.println(etatbouton2);
    delay(10);
  }
  
  etatbouton3 = digitalRead(bouton3);
  
  if (etatbouton3 == LOW) {
    servo_3.write(0);
    Serial.println(etatbouton3);
    delay(10);
  }
  else {
    servo_3.write(180);
    Serial.println(etatbouton3);
    delay(10);
  }
  
  etatbouton4 = digitalRead(bouton4);
  
  if (etatbouton4 == LOW) {
    servo_4.write(0);
    Serial.println(etatbouton4);
    delay(10);
  }
  else {
    servo_4.write(180);
    Serial.println(etatbouton4);
    delay(10);
  }
  
  etatbouton5 = digitalRead(bouton5);
  
  if (etatbouton5 == LOW) {
    servo_5.write(0);
    Serial.println(etatbouton5);
    delay(10);
  }
  else {
    servo_5.write(180);
    Serial.println(etatbouton5);
    delay(10);
  }
}