import socket
import threading

#Configuracion del servidor
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(5) #El servidort escucha hasta 5 conexiones, limitamos a 5 en este caso
    print("Servidor TCP activo en localhost:5000 y esperando conexiones... ")

     # Iniciar un hilo para escuchar comandos en la consola del servidor
    thread_commands = threading.Thread(target=listener, args=(server,))
    thread_commands.start()

    while True:
        conection, direction = server.accept()
        print(f"Conexión establecida con {direction}")

        while True:
            msg = conection.recv(1024).decode('utf-8')
            if not msg:
                break

            print(f"Mensaje recibido: {msg}")

             # Convertir el mensaje a minúsculas para la comparación
            normalized_msg = msg.lower()

            if normalized_msg == "desconexion":
                print("Cliente solicitó desconexión. Cerrando conexión...")
                conection.close()
                break
            elif normalized_msg == "hola servidor":
                answer = "HOLA CLIENTE"
                conection.send(answer.encode('utf-8'))
                print(f"Respuesta enviada: {answer}")
            else:
                # Responder con el mensaje en mayúsculas y agregar "CLIENTE"
                answer = msg.upper()
                conection.send(answer.encode('utf-8'))
                print(f"Respuesta enviada: {answer}")


    server.close()
    print("Servidor cerrado. ")

def listener(server):
    while True:
        command = input().lower()  # Normalizar la entrada a minúsculas
        if command == "cerrar servidor":
            print("Cerrando el servidor...")
            server.close()
            break

if __name__ == "__main__":
    start_server()             