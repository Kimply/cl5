import socket

ip=input('Enter ip server :')
port=input('\nEnter port server :')


        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
while(1):
    try: 
        s.connect((ip, int(port)))
        while True:
           message=input("your message: ")+" "
           s.send(message.encode('utf-8'))
    except socket.error as e:
        print(e)

  




            