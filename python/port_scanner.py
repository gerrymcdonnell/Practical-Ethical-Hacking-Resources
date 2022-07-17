import sys
from datetime import datetime as dt
import socket

from rx import catch

if len(sys.argv) == 3:
  target = socket.gethostbyname(sys.argv[1]) # translates host to ipv4
  #get port range from cmd line
  port_range=sys.argv[2].split('-')
  start_port=int(port_range[0])
  end_port=int(port_range[1])
elif len(sys.argv) == 2:
  start_port=1
  end_port=1000
  target = socket.gethostbyname(sys.argv[1]) # translates host to ipv4
else:
  print("Invalid number of args")
  print("Syntax: python3 port_scanner.py [ip/hostname] [port: start-end eg 1-80]")

print("Scannning target: " + target)
print("Time started: " + str(dt.now()))
print('-' * 50)


try:
  print("scanning ports: {} to {}".format(start_port,end_port))
  for port in range(start_port,end_port):
    #print("scanning port {}".format(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print("port {} is open".format(port))
    s.close 
except KeyboardInterrupt:
  print('\nExitting...')
  sys.exit()
except socket.gaierror:
  print("Hostname couldn't be resolved")
  sys.exit()
except socket.error:
  print("Couldn't connect to server")
  sys.exit()
