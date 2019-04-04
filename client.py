import socket 
from time import sleep 

host = '10.42.19.202'
port = 5005


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

while True:
	unknown = "unknown"
	kill = "kill"
	test = "test"
	command = input("Enter command: ")
	if command == 'kill':
		s.send(str.encode(command))
		break 
	s.send(str.encode(command))
	reply = s.recv(1024)
	print(reply)

s.close()
