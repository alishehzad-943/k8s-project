Deploy Flask App on KIND (Kubernetes in Docker) Using EC2
Step-by-Step Implementation
Step 1: Setup EC2 Instance (Ubuntu t2.medium)
Login to AWS Console → EC2 Service
Launch Instance

Name: k8s

AMI: Ubuntu 22.04 LTS

Instance type: t3.micro

Key pair: Create or choose existing

Security Group Rules:

SSH (22)

HTTP (80)

Custom TCP 30007 (Flask App)

Click Launch

Connect via SSH
ssh -i mykey.pem ubuntu@<EC2_PUBLIC_IP>

Step 2: Install Docker
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
docker --version

Step 3: Install KIND and Kubectl
Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl
kubectl version --client

Install KIND
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind version

Create kind-config.yaml

1 control-plane node

Port mappings for 80 and 443

Step 4: Create KIND Cluster
kind create cluster --name flask-cluster
kubectl cluster-info
kubectl get nodes

Step 5: Create a Kubernetes Namespace
namespace.yaml

(Create file manually)

Apply Namespace
kubectl apply -f namespace.yaml
kubectl get ns

Step 6: Create a Flask Application
Project Directory
mkdir flask-app && cd flask-app

Files Required

app.py

requirements.txt

Dockerfile

Step 7: Build and Push Docker Image
docker login
docker build -t <dockerhub-username>/flask-kind:latest .
docker push <dockerhub-username>/flask-kind:latest

Step 8: Create Kubernetes Deployment & Service
Files Needed

flask-deployment.yaml

flask-service.yaml

Apply Deployment
kubectl apply -f flask-deployment.yaml
kubectl get pods -n flask-namespace
kubectl get svc -n flask-namespace

Step 9: Access Flask Application
Expose Pod using Port Forwarding
kubectl port-forward svc/flask-service 5000:5000 -n flask-namespace

Open in Browser
http://<EC2_PUBLIC_IP>:5000
