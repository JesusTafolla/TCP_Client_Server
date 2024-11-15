import socket

#Client Configuration
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print("Cliente conectado al servidor en localhost:5000")

    while True:
        msg = input("Ingresa un mensaje para comunicarte con el servidor:")

        #Enviar mensaje al servidor
        client.send(msg.encode('utf-8'))

        # Convertir el mensaje a minúsculas para la comparación
        normalized_msg = msg.lower()

        if normalized_msg == "desconexion":
            print("Solicitando desconexion del servidor... ")
            client.close()
            break
        else:
            #Recibir y mostrar el mensaje de la respuesta del servidor
            answer = client.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {answer}")

if __name__ == "__main__":
    start_client()