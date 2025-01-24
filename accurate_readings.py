#define trigger 20
#define echo 21
float duration=0,distance=0;
void setup() {
 Serial.begin(115200);
 pinMode(trigger,OUTPUT);
 pinMode(echo,INPUT);
 delay(1000);
}
void loop() {
 digitalWrite(trigger,LOW);
 delayMicroseconds(2);
 digitalWrite(trigger,HIGH);
 delayMicroseconds(10);
 digitalWrite(trigger,LOW);
 duration=pulseIn(echo,HIGH);
 distance=duration*340/20000;
 Serial.print(distance);
 Serial.println("cm");
 delay(500);
}
