# Dockerfile for Product Page (Python)
#Imagen python 
FROM python:3.7.7-slim


ENV GROUPO_NUMERO=47

COPY ./practica_creativa2/bookinfo/src/productpage ./productpage

WORKDIR productpage

#Intalar las librerías definidas en el fichero requirements.txt
RUN python3 -m pip install -r requirements.txt


#Ejecutar el archivo productpage
CMD ["python", "productpage.py", "9080"]
