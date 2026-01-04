import usocket, socket, dht, machine
from machine import Pin, I2C
from ccs811factory import CCS811Factory

envsensor = dht.DHT11(Pin(16))
gassensor = CCS811Factory(I2C(scl=Pin(5), sda=Pin(4)))
pirsensor = Pin(13, Pin.IN)

def web_page(temp, humid, eco2, tvoc, motion):
  html = """NanoAPI 1 TemperatureC """ + str(temp) + """ HumidityR% """ + str(humid) + """ eCO2ppm """ + str(eco2) + """ TVOCppb """ + str(tvoc) + """ Motion """ + str(motion)
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

print('Ready for connections')

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  envsensor.measure()
  temp = envsensor.temperature()
  humid = envsensor.humidity()
  gassensor.temperature = temp
  gassensor.humidity = humid
  eco2 = gassensor.eco2
  tvoc = gassensor.etvoc
  motion = pirsensor.value()
  print(gassensor.eco2, "ppm and ", gassensor.etvoc, "ppb")
  response = web_page(temp, humid, eco2, tvoc, motion)
  conn.send('HTTP/1.1 200 OK\r\n')
  conn.send('Content-Type: text/html\r\n')
  conn.send('Connection: close\r\n\r\n')
  conn.sendall(response)
  conn.close()




