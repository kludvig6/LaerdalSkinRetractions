# LaerdalSkinRetractions
Repository for creating retractions in silicon skin using a setup with an Arduino Uno controlling valves, as well as a TTPVentus disc pump. The repository also includes an app to control the reatractions. Everything is executed on the host computer connected to the Arduino and the pump. See guide at the bottom of the document.

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

## Complete guide
To run the program, simply run main.py. This program starts the hardware and the app using threading. For those unfamiliar with threading, this means splitting up CPU resources into two processes running simultaneously. This allows the script to control the hardware in the background, while using the app as control input.

The app is written using the Kivy-library. Kivy is a framwork for creating cross platform apps. It is less used than for example Java, but since it is written using Python, for most people it will be easy for creating quick app sketches to control your prototypes.

The layout of the app is written in breathing.kv. The name of the kv-file should be the same as the name of the app: BreathinApp -> breathing.kv. To fill in the app page, your create layout objects which you fill with text, buttons and images. All the labels can have a background, defined by canvas.before. This allows for background pictures and different coloured backgrounds. The buttons all have an id and a corresponding callback-function written in MyLayout() in BreathingApp.py. These callbacks change the colour of the buttons and switches the background picture of certain labels to show which retractions are showing. Additionally, the callbacks change global variables defined in global_hw_car.py.

The global variables are used in HardwareControl.py to enable and disable the different retractions. The HarwareControl class in HardwareControl.py has a member function called breathing, which is used to simulate breathing and retractions. It runs continuosly. At each breath, the valves are opened or closed, the TTPVentus pump is activated, and breathing sounds are played. 