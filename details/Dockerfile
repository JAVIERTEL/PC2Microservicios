# Dockerfile for Details (Ruby)

#Imagen base a utilizar ruby:2.7.1-slim
FROM ruby:2.7.1-slim

#Copiar el fichero  detail.rb en la ruta /opt/microservices/ dentro del contenedor
COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/details.rb
#Movernos al directorio de ejecuión
WORKDIR /opt/microservices/

#Especificar dos variables de entorno
ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true
#Exponer el puerto 9080
EXPOSE 9080
#Ejecutar el fichero details.rb
CMD ["ruby", "details.rb", "9080"]
