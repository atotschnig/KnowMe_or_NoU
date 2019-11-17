// Boston Hacks 2019 Project - KnowMe or NoU
// Authors: Julia Fowler, Aria Rens, Sarah Santoso, Agnes Totschnig and Saumyaa Verma
// Date: 16th of November 2019

int ledPin = 13;    // choose the pin for the LED
int inputPin1 = 4;   // red button
int inputPin2 = 5;   // yellow button
int inputPin3 = 6;   // blue button
int inputPin4 = 7;   // green button
int inputPin5 = 8;   // red button 2
int inputPin6 = 9;   // yellow button 2
int inputPin7 = 10;   // blue button 2
int inputPin8 = 11;   // green button 2
int sensorValue1;
int sensorValue2;
int sensorValue3;
int sensorValue4;
int sensorValue5;
int sensorValue6;
int sensorValue7;
int sensorValue8;

void setup()
{
  pinMode(ledPin, OUTPUT);  // declare LED as output
  pinMode(inputPin1, INPUT); // declare red push button as input
  pinMode(inputPin2, INPUT); // declare yellow push button as input
  pinMode(inputPin3, INPUT); // declare blue push button as input
  pinMode(inputPin4, INPUT); // declare green push button as input
  pinMode(inputPin5, INPUT); // declare red 2 push button as input
  pinMode(inputPin6, INPUT); // declare yellow 2 push button as input
  pinMode(inputPin7, INPUT); // declare blue 2 push button as input
  pinMode(inputPin8, INPUT); // declare green 2 push button as input

  Serial.begin(9600);
}
 
void loop()
{
  sensorValue1 = digitalRead(inputPin1);  // read input value
  sensorValue2 = digitalRead(inputPin2);  // read input value
  sensorValue3 = digitalRead(inputPin3);  // read input value
  sensorValue4 = digitalRead(inputPin4);  // read input value
  sensorValue5 = digitalRead(inputPin5);  // read input value
  sensorValue6 = digitalRead(inputPin6);  // read input value
  sensorValue7 = digitalRead(inputPin7);  // read input value
  sensorValue8 = digitalRead(inputPin8);  // read input value
  Serial.print(sensorValue1);         // send data to serial
  Serial.print(sensorValue2);         // send data to serial
  Serial.print(sensorValue3);         // send data to serial
  Serial.print(sensorValue4);         // send data to serial
  Serial.print(sensorValue5);         // send data to serial
  Serial.print(sensorValue6);         // send data to serial
  Serial.print(sensorValue7);         // send data to serial
  Serial.println(sensorValue8);         // send data to serial
}
