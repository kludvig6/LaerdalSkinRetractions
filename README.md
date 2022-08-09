# LaerdalSkinRetractions
Repository for creating retractions in silicon skin using a setup with an Arduino Uno controlling valves, as well as a TTPVentus disc pump. The repository also includes an app to control the reatractions. Everything is executed on the host computer connected to the Arduino and the pump.

## Setup
### Requirements
kivy
playsound
threading
time
serial
pyfirmata

### Paths
*dir_path* in **HardwareControl.py** must be set to the local path of the repository (could probably use **os** package).

The *COM*-ports used in line 12 and 27 in **HardwareControl.py** must be set to the appropriate ports.

## Hardware
The setup utilizes a TTPVentus Evaluation kit, a piezoelectric disc pump, for breathing and retractions. Retractions are controlled using a setup consisting of an Arduino Uno together with transistors and solenoid valves. When the valves are open, air is sucked out from cavities in a silicon skin.

## Notes
### Note on Kivy library
In kivy, .kv-files are used as a formatting file, similar to XAML-files in .NET-programming. The central part of **breathing.kv** is the buttons. They are given a specific ID and callback-functions implemented in **BreathingApp.py**.

### Note on threading
Threading is used extensively to synchronize breathing, retractions and breathing sounds, as well as running hardware and app concurrently. Though the different threads use shared resources, a lock has not been implemented. This is because multiple threads will not overwrite the shared resources simultaneously. Though reading and writing of the resource might happen simultaneously, this was not seen as a critical problem since it will not cause the system to fail.