3.1 Lo primero ha sido comprobar que tenemos descargado docker-compose :
```
sudo apt update 

sudo apt upgrade 

sudo apt install docker.io 

sudo apt install docker-compose 
```
3.2 A continuación creamos cuatro ficheros DockerFile uno para cada microservicio en el idioma exigido. En el caso del DockerFile de java ya venía hecho y tan solo hemos modificado la línea COPY para referenciar de forma correcta al directoria de nuestra app. 

3.3 Después hemos programado el fichero docker-compose.yml describe cómo deben ejecutarse los contenedores, qué imágenes usar, qué puertos exponer, qué variables de entorno establecer, entre otras configuraciones. 

3.4 Por último un fichero llamado comando2.py para crear las imágenes y construir los contenedores. 

Para la ejecución tendremos que clonar el repositorio en nuesta mv
```
cd PC2Microservicios
git clone https://github.com/JAVIERTEL/PC2Microservicios.git 
```
Por último mediante:
```
sudo python3 ./comandos2.py . 
```
Se subirá la práctica basada en microservicios y podremos acceder a ella mediante : 

http://<ip_pública>:9080 




 
