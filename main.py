import usocket, socket, dht, machine, CCS811
from machine import Pin, I2C

envsensor = dht.DHT11(Pin(16))
i2c = I2C(scl=Pin(5), sda=Pin(4))
gassensor = CCS811.CCS811(i2c)

def web_page(temp, humid, eco2, tvoc):
  html = """NanoAPI 1 TemperatureC """ + str(temp) + """ HumidityR% """ + str(humid) + """ eCO2ppm """ + str(eco2) + """ TVOCppb """ + str(tvoc)
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
  eco2 = gassensor.eCO2
  tvoc = gassensor.tVOC
  print(gassensor)
  response = web_page(temp, humid, eco2, tvoc)
  conn.send('HTTP/1.1 200 OK\r\n')
  conn.send('Content-Type: text/html\r\n')
  conn.send('Connection: close\r\n\r\n')
  conn.sendall(response)
  conn.close()




