// Boston Hacks 2019 Project - KnowMe or NoU
// Authors: Julia Fowler, Aria Rens, Sarah Santoso, Agnes Totschnig and Saumyaa Verma
// Date: 16th of November 2019

int ledPin = 13;    // choose the pin for the LED
int inputPin = 7;   // choose input pin 7 for the push button
 
void setup()
{
  pinMode(ledPin, OUTPUT);  // declare LED as output
  pinMode(inputPin, INPUT); // declare push button as input
}
 
void loop()
{
  int pushed = digitalRead(inputPin);  // read input value
  if (pushed == HIGH) // check if the input is HIGH    
    digitalWrite(ledPin, LOW);  // turn LED OFF
  else
    digitalWrite(ledPin, HIGH);  // turn LED ON
}
