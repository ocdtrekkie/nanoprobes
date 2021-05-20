import usocket, socket, dht, machine
from machine import Pin

envsensor = dht.DHT11(Pin(16))

def web_page(temp, humid):
  html = """NanoAPI 1 TemperatureC """ + str(temp) + """ HumidityR% """ + str(humid)
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
  response = web_page(temp, humid)
  conn.send('HTTP/1.1 200 OK\r\n')
  conn.send('Content-Type: text/html\r\n')
  conn.send('Connection: close\r\n\r\n')
  conn.sendall(response)
  conn.close()




