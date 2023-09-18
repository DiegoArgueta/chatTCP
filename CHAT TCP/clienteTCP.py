import socket
import threading

usuarioNombre= input("Ingrese el usuario: ")
host='127.0.0.1'
port= 55555

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))

def recibir_mensaje():
    while True:
        
        try:
            message=client.recv(1024).decode('utf-8')
        
            if message== "Usuario":
                client.send(usuarioNombre.encode('utf-8'))
            else:
                print(message)
        except:
            print("Un error surgio durante el mensaje")
            client.close()
            break

def escribirMensaje():
    message= f"{usuarioNombre}: {input('')}"
    client.send(message.encode('utf-8'))
    
recibir_thread=threading.Thread(target=recibir_mensaje)      
recibir_thread.start()


write_thread=threading.Thread(target=escribirMensaje)      
write_thread.start()


