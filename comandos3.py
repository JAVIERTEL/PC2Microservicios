import subprocess
import time

def run_command(command):
    subprocess.call(command, shell=True)


# Iniciamos un cluster de Kubernetes con 5 nodos
run_command("minikube start --driver=docker -p pc2 --nodes 5")

# Cambiamos al perfil que acabamos de crear
run_command("minikube profile pc2")

# Desplegamos los servicios y deployments
run_command("minikube kubectl apply -- -f .")

# Esperamos hasta que todos los pods se hayan iniciado
while (str(subprocess.check_output(["minikube kubectl get pods"], shell=True)).count("Running") < 9):
    time.sleep(1)

# Abrimos la web de product-page
run_command("minikube service product-page")
