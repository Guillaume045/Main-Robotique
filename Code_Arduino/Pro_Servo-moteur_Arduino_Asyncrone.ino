#include <Servo.h>

int boutons[] = {2, 3, 4, 5, 6};
int etatsBoutons[] = {0, 0, 0, 0, 0};
Servo servos[5];
int angles[] = {0, 0, 0, 0, 0};

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 5; i++) {
    pinMode(boutons[i], INPUT);
    servos[i].attach(12 - i); // Les servos sont connectés aux broches 12, 11, 10, 9, 8
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    etatsBoutons[i] = digitalRead(boutons[i]);

    if (etatsBoutons[i] == LOW) {
      angles[i] = 0;
    } else {
      angles[i] = 180;
    }
    servos[i].write(angles[i]);
    Serial.print("Bouton ");
    Serial.print(i + 1);
    Serial.print(": ");
    Serial.println(etatsBoutons[i]);
    delay(10);
  }
}
