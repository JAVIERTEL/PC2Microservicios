# Dockerfile for Ratings (Node.js)
#Imagen base a utilizar node:12.18.1-slim
FROM node:12.18.1-slim
#Copiar los ficheros package.json y ratings.js a la ruta /opt/microservices/ dentro del contenedor.
COPY ./practica_creativa2/bookinfo/src/ratings/* /opt/microservices/

#Especificar la variable de entorno SERVICE_VERSION con valor v1
ENV SERVICE_VERSION=v1
#Copiar los ficheros package.json y rating.js a la ruta /opt/microservices/
WORKDIR /opt/microservices/

# Instalar las dependencias
RUN npm install
# Exponer el puerto 9080 
EXPOSE 9080
#Ejecutar el fichero ratings.js, usando la instrucción node y añadir el puerto ex:
CMD ["node", "ratings.js", "9080"]


