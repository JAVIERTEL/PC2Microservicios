import subprocess

def run_command(command):
    subprocess.call(command, shell=True)

# Importar la aplicación
run_command("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
#Compilar y empaquetar los ficheros necesarios ejecutando, dentro de la ruta src/reviews, el siguiente comando:
run_command('cd practica_creativa2/bookinfo/src/reviews && docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
run_command('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')


# Crear las imágenes de cada uno de los servicios de acuerdo al siguiente formato de nombre: <numero_de_grupo>/<nombre_de_microservicio
run_command("docker build -t g47/product-page -f ./product-page/Dockerfile .")
run_command("docker build -t g47/details -f ./details/Dockerfile .")
run_command("docker build -t g47/ratings -f ./ratings/DockerFile .")

# Incluir la creación de las tres versiones del servicio de reviews. Para especificar la versión se hace uso de la variable de entorno SERVICE_VERSION cuyos valores pueden ser v1, v2 o v3
#Review v1 => Sin estrellas 
run_command ("docker build -t g47/reviews-v1 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color='black' .")
run_command ("docker build -t g47/reviews-v2 -f ./reviews/Dockerfile --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color='black' .")
run_command ("docker build -t g47/reviews-v3 -f ./reviews/Dockerfile --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color='red' .")


run_command ("docker-compose up")