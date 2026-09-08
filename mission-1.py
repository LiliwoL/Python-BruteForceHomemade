# https://www.paramiko.org/
import paramiko
from pyfiglet import Figlet

# Affichage
figlet = Figlet(font='standard')

print(f.renderText("Python BruteForce Homemade"))

# Infos de la machine cible
remoteHost="172.16.3.254"
username="userfaible"
password="userfaible"
port=22

pirate=False

try:	
	# Création du client SSH
	client = paramiko.client.SSHClient()

	# Set the policy to accept any host key
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	# Connexion avec les variables de la machine cible
	client.connect(remoteHost, username=username, password=password, port=port)
	pirate=True

except:
	# En cas d'échec de la connexion, on arrive ici
	pirate=False

	print("Connexion échouée, vérifiez les informations de connexion et l'état du serveur SSH.")
	client.close()

# Si la connexion a réussi
if pirate:
	# Commande à exécuter sur la machine cible
	command = "tail /etc/passwd"

	# Exécution de la commande et récupération de la sortie
	_stdin, _stdout, _stderr = client.exec_command(command)

	# Affichage
	print ("Sortie")
	print( _stdout.read().decode() )

# Fermeture du client SSH
client.close()