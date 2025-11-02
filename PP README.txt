## Women Safety App (Simulation)

A Tkinter-based Women Safety App Simulation built in Python.
This project demonstrates multiple safety features such as SOS alerts, fake calls, guardian tracking, and legal rights guides using a simple GUI and logic-based simulations.

---

## FEATURES

1. TRIGGER SOS

   * Sends a simulated emergency alert using desktop notifications.
   * Logs SOS triggers with timestamps in a local file (sos_log.txt).
   * Displays confirmation pop-up after triggering.

2. FAKE CALL GENERATOR

   * Simulates an incoming fake call from any name (e.g., Mom, Boss, Police).
   * User can set a custom delay (1–30 seconds) before the fake call rings.
   * Displays a fake call window with “Answer” and “Reject” buttons.

3. SECRET CODE TRIGGER

   * Hidden emergency feature.
   * If user enters the secret phrase: "i forgot my homework", SOS alert is triggered.
   * Otherwise, it shows a "Safe" message.

4. GUARDIAN MODE SIMULATION

   * Simulates a safe route tracking system using pre-defined coordinates.
   * Prints current simulated location in the console.
   * Randomly detects “route deviation” and triggers an SOS alert if detected.

5. QUICK LAW & RIGHTS GUIDE

   * Displays key legal rights and helpline information:

     * Workplace Harassment Helpline: 181
     * National Women’s Helpline: 1091 / 181
     * Right to dignity when stopped by police

---

## GUI OVERVIEW

* Header: Women Safety App (displayed in teal-blue)
* Buttons: Each feature accessible with one click
* Theme: Dark background (#222831) with accent-colored buttons
* Framework: Built using Tkinter for GUI

---

## REQUIREMENTS

Install dependencies before running:

pip install plyer

Used Modules:

* tkinter (built-in)
* plyer (for notifications)
* time, random (standard Python libraries)

---

## HOW TO RUN

1. Save the script as "women_safety_app.py"

2. Open the folder in Command Prompt or IDE terminal

3. Run the program using:

   python women_safety_app.py

4. The GUI window will open with all features ready to use.

---

## LOG FILES

File: sos_log.txt
Purpose: Stores timestamps of all SOS triggers.

Example content:
SOS triggered at Mon Oct 27 09:25:31 2025

---

## TECH STACK

* Language: Python 3.x
* GUI Framework: Tkinter
* Notifications: Plyer
* Platform: Cross-platform (Windows, macOS, Linux)

---

## FUTURE ENHANCEMENTS

* Integrate real GPS tracking (via geopy or APIs)
* Add SMS/email alert system for emergency contact
* Include Dark/Light mode toggle
* Add AI-based alert detection (camera or voice)

---

## AUTHORS

Deboleena Debroy
Disha Roy
Avanti Marathe



