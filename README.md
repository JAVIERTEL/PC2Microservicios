3.1 Lo primero ha sido comprobar que tenemos descargado docker-compose :
sudo apt update 

sudo apt upgrade 

sudo apt install docker.io 

sudo apt install docker-compose 

3.2 A continuación creamos cuatro ficheros DockerFile uno para cada microservicio en el idioma exigido. En el caso del DockerFile de java ya venía hecho y tan solo hemos modificado la línea COPY para referenciar de forma correcta al directoria de nuestra app. 

3.3 Despuñes hemos programado el fichero docker-compose.yml describe cómo deben ejecutarse los contenedores, qué imágenes usar, qué puertos exponer, qué variables de entorno establecer, entre otras configuraciones. 

3.4 Por último un fichero llamado comando2.py para crear las imágenes y construir los contenedores. 

Para la ejecución tendremos que clonar
 
git clone https://github.com/JAVIERTEL/PC2Microservicios.git 

Por último mediante:
sudo python3 ./comandos2.py . 

Se subirá la práctica basada en microservicios y podremos acceder a ella mediante : 

http://<ip_pública>:9080 
ChatGPT
Segmentación de una Aplicación Monolítica en Microservicios utilizando Docker Compose
3.1 Instalación de Docker Compose
Para iniciar el proceso, es necesario asegurarse de tener Docker Compose instalado. Puedes realizarlo ejecutando los siguientes comandos:

bash
Copy code
sudo apt update
sudo apt upgrade
sudo apt install docker.io
sudo apt install docker-compose
3.2 Creación de Dockerfiles y Adaptación del de Java
A continuación, se crean cuatro archivos Dockerfile, uno para cada microservicio en el lenguaje especificado. En el caso del Dockerfile para Java, generalmente ya viene preconfigurado y solo se requiere modificar la línea COPY para hacer referencia al directorio de la aplicación.

3.3 Configuración del archivo docker-compose.yml
Luego, se programa el archivo docker-compose.yml, el cual describe cómo deben ejecutarse los contenedores, qué imágenes utilizar, qué puertos exponer, qué variables de entorno establecer, entre otras configuraciones.

3.4 Creación del Script comando2.py
Finalmente, se crea un archivo llamado comando2.py para facilitar la construcción de imágenes y contenedores.

Ejecución
Para ejecutar este proceso, clona el repositorio desde el siguiente enlace:

bash
Copy code
git clone https://github.com/JAVIERTEL/PC2Microservicios.git
Posteriormente, utiliza el siguiente comando para iniciar la práctica basada en microservicios:

bash
Copy code
sudo python3 ./comandos2.py
Una vez completado, la aplicación estará disponible en:

http://<ip_pública>:9080



 
