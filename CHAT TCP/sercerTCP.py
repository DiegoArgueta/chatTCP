import socket
import threading


host='127.0.0.1'
port= 55555

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen()
print(f"El servidor esta escuchando el host: {host} y el puerto: {port}")

clientes=[]
usuarios=[]

def broadcast(message,_cliente):
    for cliente in clientes:
        if cliente!= _cliente:
            cliente.send(message)

def handle_message(cliente):
    while True:
        try:
            message=cliente.recv(1024)
            broadcast(message,cliente)
        except:
            index= clientes.index(cliente)
            usuario= usuarios[index]        
            broadcast(f"Chat bot {usuario} desconectado del chat".encode('utf-8'))  
            clientes.remove(cliente) 
            usuarios.remove(usuario)
            cliente.close()
            break
            
def recibirConexion():
    while True:
        cliente,adress=server.accept()
        cliente.send("Usuario".encode('utf-8'))
        usuario= cliente.recv(1024).decode('utf-8')
        clientes.append(cliente)
        usuarios.append(usuario)
    
        print(f"{usuario} esta conectado con {str(adress)}")
    
        message=f" Chat TCP: {usuario} se unio al chat".encode('utf-8')
        broadcast(message,cliente)
        cliente.send("Conectado al servidor".encode('utf-8'))
        thread= threading.Thread(target=handle_message,args=(cliente,))
        thread.start()

recibirConexion()