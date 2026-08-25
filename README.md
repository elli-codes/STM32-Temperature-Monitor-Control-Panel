# STM32-Temperature-Monitor-Control-Panel
A desktop-based control panel for monitoring temperature and controlling external devices through UART serial communication with an STM32 microcontroller.

This project combines Python, Tkinter, PySerial, and STM32 embedded C to demonstrate communication between a Linux-based desktop application and an embedded system. The graphical control panel allows an authorized user to control an LED, monitor the current temperature, display the system time, and control a simulated cooling system.

Note: The STM32 firmware was developed and programmed from a Windows environment, while the Python GUI application runs on Linux and communicates with the microcontroller through a USB-to-Serial connection.

✨ Features
🔐 Password-protected control panel
💡 Turn an LED ON and OFF remotely
🌡️ Read temperature data from the STM32 ADC
🕒 Display the current system time
❄️ Control a cooler system ON and OFF
🔄 UART communication between Python and STM32
⚡ DMA-based UART reception
📊 ADC data acquisition using DMA
🖥️ Simple graphical user interface built with Tkinter

The Python application sends commands to the STM32 through a serial connection. The STM32 receives the commands and performs the requested action, such as controlling GPIO pins or sending temperature data back to the computer.

The firmware initializes the ADC, DMA, UART, GPIO, and LCD peripherals and processes commands received through UART.
💻 Software and Technologies
Desktop Application
Python 3
Tkinter
PySerial
Embedded Firmware
C
STM32 HAL
STM32CubeIDE / STM32 development tools
UART with DMA
ADC with DMA
🐧 Running the Python Application on Linux

Password Authentication

The user must enter the correct password before the control buttons become available. The GUI sends authentication information to the STM32, which can provide additional feedback through the connected hardware.

📽️Working demo video available on YouTube:https://www.youtube.com/@EllisLearningJourney 
