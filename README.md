#Step-by-Step Implementation
#Step 1: Setup EC2 Instance (Ubuntu t2.medium)
#Login to AWS Console → EC2 Service.

3Launch Instance:
Name: k8s
AMI: Ubuntu 22.04 LTS
Instance type: t3micro 
Key pair: Create/Choose an existing one
Security group: Allow SSH (22), HTTP (80), Custom TCP 30007 (Flask App) 
Click Launch.


#Connect via SSH:
ssh -i mykey.pem ubuntu@<EC2_PUBLIC_IP>


#Step 2: Install Docker
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
docker --version


#Step 3: Install KIND and Kubectl
Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl
kubectl version --client


#Install KIND:
curl -Lo ./kind https://kind.sigs.k8s.io/dl/latest/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind version


#Write Kind config.yml with:
1 control-plane node (with Docker image)
Port mappings for 80 and 443 (TCP)


#Step 4: Create KIND Cluster
kind create cluster --name flask-cluster
kubectl cluster-info
kubectl get nodes


#Step 5: Create a Kubernetes Namespace
#Namespaces help organize and isolate resources in a cluster.
#Write simple Kubernetes Namespace YAML you can use for your Flask app:
      namespace.yml
kubectl apply -f namespace.yaml
kubectl get ns



#Step 6: Create a Flask Application
#Project Directory:
mkdir flask-app && cd flask-app
app.py:
requirements.txt:
Dockerfile:



#Step 7: Build and Push Docker Image (If you want to push docker file)
docker login
docker build -t <dockerhub-username>/flask-kind:latest .
docker push <dockerhub-username>/flask-kind:latest


#Step 8: Create Kubernetes Deployment & Service in Namespace
flask-deployment.yaml:
flask-service.yaml:

#Apply deployment to namespace:

kubectl apply -f flask-deployment.yaml
kubectl get pods -n flask-namespace
kubectl get svc -n flask-namespace


#Step 9: Access Flask Application
#Since KIND runs inside Docker, expose the port using kubectl port-forward:
kubectl port-forward svc/flask-service 5000:5000 -n flask-namespace

#Open in browser:
#http://<EC2_PUBLIC_IP>:5000

