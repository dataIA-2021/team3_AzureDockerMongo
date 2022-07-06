# team3_AzureDockerMongo
Projet Azure Docker Mongo App de Silvain, César ,Tess et Célia

Creation de l'adresse IP:
az network public-ip create -g groupe3TCCS -n groupe3Ip --dns-name groupe3ip --allocation-method Static

Creation du Réseau:
az network vnet create --name groupe3VirtualNetwork --resource-group groupe3TCCS --address-prefixes 10.0.0.0/16 --subnet-name groupe3Subnet --subnet-prefixes 10.0.0.0/24

Creation de la machine virtuelle:
az vm create -n groupe3S -g groupe3TCCS --size Standard_D2s_v3 --image UbuntuLTS --vnet-name groupe3VirtualNetwork --subnet groupe3Subnet --public-ip-address groupe3Ip --admin-username groupe3 --admin-password groupe3GRE2022! --ssh-key-values @~/.ssh/id_rsa.pub



ssh groupe3@groupe3Ip.westeurope.cloudapp.azure.com
mdp : groupe3GRE2022!

Installations docker / lazydocker
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io mongodb-clients python3-pip
# lazydocker
# https://github.com/jesseduffield/lazydocker
# Ajout group docker
sudo usermod -aG docker $USER


connexion à Mongodb
mongo mongodb://172.17.0.2:27017
