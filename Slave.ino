#include <Wire.h>

int sensorStatus = 0;

void setup()
{
  Wire.begin(4);
  Wire.onReceive(configureSensor);
  Wire.onRequest(sendAmbientLightLevel);
  Serial.begin(9600);
}

void loop()
{
}

void configureSensor(int numBytesReceived)
{
  if (Wire.available() > 0) {
    sensorStatus = Wire.read();
  }
}

void sendAmbientLightLevel()
{
  if (sensorStatus == 1) {
    int lightLevel = rand() % 100 + 1;
    Wire.write(lightLevel);
  }
}
