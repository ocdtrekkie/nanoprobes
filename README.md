Nanoprobes are ESP-based home automation sensing units. The idea here is to create simple platforms that can be distributed around a house for a main server to collect data from. In the interests of being standards-based as possible, the goal is to respond over HTTP with a simple plaintext format that can be easily parsed by any language.

The initial test nanoprobe currently programmed here is a ESP8266-powered Feather HUZZAH with a DHT11 sensor assigned to pin 16 and a CCS811 attached to the I2C bus.

Most of this project is based on tutorials found at https://randomnerdtutorials.com

CCS811.py was grabbed from https://github.com/stigtsp/CCS811-micropython

I used uPyCraft V1.1 to flash the device.