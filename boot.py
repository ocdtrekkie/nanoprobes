# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import uos, machine, network, time
import secrets
from machine import Pin

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

#import webrepl

#webrepl.start()

gc.collect()

led = Pin(2, Pin.OUT)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(secrets.ssid, secrets.wpa)

while not sta_if.isconnected():
  led.off()
  time.sleep(0.5)
  led.on()
  time.sleep(0.5)

led.off()
print('network config:', sta_if.ifconfig())


