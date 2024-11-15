# Cliente y Servidor TCP en Python

Este proyecto implementa un servidor y un cliente TCP en Python que pueden comunicarse en la misma máquina a través de `localhost` en el puerto `5000`. Este ejemplo práctico demuestra conocimientos de programación en Python y el uso de sockets para la comunicación en red.

## Descripción

El servidor TCP espera conexiones de los clientes y responde a los mensajes recibidos devolviendo el contenido en mayúsculas. Si se recibe el mensaje "DESCONEXION", el servidor cierra la conexión con ese cliente, pero sigue disponible para nuevas conexiones.

El cliente TCP permite al usuario ingresar mensajes, enviarlos al servidor y mostrar la respuesta recibida. Cuando el usuario ingresa "DESCONEXION", el cliente finaliza la conexión y se cierra.

## Características

- **Servidor**: Escucha conexiones en `localhost:5000` y responde en mayúsculas.
- **Cliente**: Permite enviar mensajes al servidor y muestra las respuestas.
- **Manejo de Desconexión**: Cierre adecuado de la conexión al recibir el mensaje "DESCONEXION".

## Requisitos Previos

- Python 3.x instalado.
- Conocimientos básicos de la línea de comandos.

## Instalación

1. Clona este repositorio o descarga los archivos `server.py` y `client.py`.
2. Asegúrate de que Python 3.x esté configurado en tu sistema.

## Uso

### 1. Ejecutar el Servidor
En una terminal, navega al directorio donde se encuentra `server.py` y ejecuta: 
bash python server.py

### 2. Al ejecutarse el server la salida esperada deberia de ser
Servidor TCP activo en localhost:5000 y esperando conexiones...

### 3. Ejecutar el Cliente
En una terminal, navega al directorio donde se encuentra `server.py` y ejecuta: 
bash python client.py

### 4. Al ejecutarse el cliente la salida esperada deberia de ser
Cliente conectado al servidor en localhost:5000
Ingresa un mensaje:


# EJEMPLO DE EJECUCION DE PRUEBAS:

## 1. MENSAJE ESTANDAR
### CLIENTE:
Ingresa un mensaje: hola servidor

### SERVIDOR (SE MUESTRA EN LA CONSOLA):
Mensaje recibido: hola servidor
Respuesta enviada: HOLA SERVIDOR

### CLIENTE (SE MUESTRA EN CONSOLA):
Respuesta del servidor: HOLA SERVIDOR

## 2. DESCONEXION
### CLIENTE:
Ingresa un mensaje: DESCONEXION

### SERVIDOR (SE MUESTRA EN LA CONSOLA):
Mensaje recibido: DESCONEXION
Cliente solicitó desconexión. Cerrando conexión...

### CLIENTE (SE MUESTRA EN CONSOLA):
Solicitando desconexión del servidor...


# NOTAS TECNICAS
1. El servidor se implementa usando socket.AF_INET y socket.SOCK_STREAM para usar un socket TCP.
2. La comunicación se realiza codificando los datos en UTF-8.
3. Se pueden personalizar la dirección IP y el puerto editando las variables en los scripts.

# MEJORAS POTENCIALES
1. Implementar soporte para múltiples clientes usando threading o asyncio.
2. Añadir manejo de errores más detallado para situaciones inesperadas.
3. Crear una interfaz gráfica básica para la interacción del cliente.

# MEJORAS IMPLEMENTADAS
1. Se tomo en cuenta que el servidor siempre estaba abierto y si se desea hacer mantenimietno o alguna actualizacion se puede realizar mediante el comando cerrarservidor al escribirlo en la terminal del servidor. Esto hara que todas las sesiones se cierren automaticamente.