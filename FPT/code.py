#include <Servo.h>

// ---------- SERVOZ DA ARMS AND BASE ---------- //
Servo baseServo;
Servo armServo1;
Servo armServo2;

// ---------- INPUTS ;D ---------- //
const int modeButton = 2;
const int joystickX = A0;
const int joystickY = A1;
const int joystickSW = 7;

// ---------- OUTPUTS ---------- //
const int buzzerPin = 4;

// ---------- RGB LED ---------- //
const int redPin = 3;
const int greenPin = 5; // Ah, wonderful green (DONT DOCK A PROFESIONALISM MARK FOR THIS PLS GREEN NEEDS APRECIATION)
const int bluePin = 6;

// ---------- MODE CONTROL ---------- //
int mode = 0;                   // 0 = idle, 1 = manual, 2 = demo
bool lastButtonState = HIGH;

// ---------- JOYSTICK BUTTON CONTROL ---------- //
bool lastJoystickState = HIGH;

// ---------- DEMO TIMING ---------- //
unsigned long lastMoveTime = 0;
bool demoStep = false;

// ---------- SETUP ---------- //
void setup() {
  baseServo.attach(9);
  armServo1.attach(10);
  armServo2.attach(11);

  pinMode(modeButton, INPUT_PULLUP);
  pinMode(joystickSW, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  // neutral pose so robot doesnt wake up angry
  baseServo.write(90);
  armServo1.write(90);
  armServo2.write(90);
}

// ---------- LOOP ---------- //
void loop() {
  checkMode();
  checkJoystickButton();
  updateLED();

  // ---------- IDLE MODE ---------- //
  if (mode == 0) {
    baseServo.write(90);
    armServo1.write(90);
    armServo2.write(90);
  }

  // ---------- MANUAL MODE ---------- //
  else if (mode == 1) {
    int xVal = analogRead(joystickX);
    int yVal = analogRead(joystickY);

    // deadzone to stop jitter (VERY IMPORTANT)
    if (abs(xVal - 512) > 40) {
      int baseAngle = map(xVal, 0, 1023, 45, 135);
      baseServo.write(baseAngle);
    }

    if (abs(yVal - 512) > 40) {
      int armAngle = map(yVal, 0, 1023, 40, 140);
      armServo1.write(armAngle);
      armServo2.write(180 - armAngle);
    }
  }

  // ---------- DEMO MODE ---------- //
  else if (mode == 2) {
    unsigned long currentTime = millis();

    if (currentTime - lastMoveTime >= 500) {
      lastMoveTime = currentTime;
      demoStep = !demoStep;

      if (demoStep) {
        baseServo.write(60);
        armServo1.write(120);
        armServo2.write(60);
      } else {
        baseServo.write(120);
        armServo1.write(60);
        armServo2.write(120);
      }
    }
  }
}

// ---------- MODE BUTTON ---------- //
void checkMode() {
  bool currentState = digitalRead(modeButton);

  if (currentState == LOW && lastButtonState == HIGH) {
    mode++;
    if (mode > 2) mode = 0;

    demoStep = false;
    lastMoveTime = millis();

    modeBeep();
    delay(250); // debounce but not cursed
  }

  lastButtonState = currentState;
}

// ---------- JOYSTICK BUTTON ---------- //
void checkJoystickButton() {
  bool currentState = digitalRead(joystickSW);

  if (currentState == LOW && lastJoystickState == HIGH) {
    joystickBeep();
    specialMove();     // 🔥 IT ACTUALLY DOES SOMETHING NOW
    delay(250);        // debounce
  }

  lastJoystickState = currentState;
}

// ---------- SPECIAL JOYSTICK MOVE ---------- //
void specialMove() {

  if (mode == 0) {
    // IDLE: small wake-up wiggle
    baseServo.write(80);
    delay(150);
    baseServo.write(100);
    delay(150);
    baseServo.write(90);
  }

  else if (mode == 1) {
    // MANUAL: quick arm grab pose
    armServo1.write(140);
    armServo2.write(40);
    delay(300);
    armServo1.write(90);
    armServo2.write(90);
  }

  else if (mode == 2) {
    // DEMO: interrupt demo and spin base
    baseServo.write(30);
    delay(300);
    baseServo.write(150);
    delay(300);
    baseServo.write(90);
  }
}

// ---------- BUZZER ---------- //
void modeBeep() {
  tone(buzzerPin, 1000, 100); // mode = high pitched beep
}

void joystickBeep() {
  tone(buzzerPin, 500, 150);  // joystick = lower pitched, longer beep DIVERSITY
}

// ---------- RGB LED ---------- //
void updateLED() {
  digitalWrite(redPin,   mode == 0);
  digitalWrite(greenPin, mode == 1); // MANUAL IS MY FAV THATS WHY ITS GREEN ;D
  digitalWrite(bluePin,  mode == 2);
}
