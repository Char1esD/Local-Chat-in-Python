import socket
import urllib.request
import os
import time

def parse_string(data,beginTag,endTag):
   result=[]
   startPos = data.find(beginTag)
   while startPos > -1:
      endPos = data.find(endTag,startPos+1)
      if endTag == -1:
         break
      else:
         result.append(data[startPos+len(beginTag):endPos])
         startPos = data.find(beginTag,endPos+1)
   return result

print("Bienvenue sur le Chat Terminal de PhoenixC")
time.sleep(2)

choix=int(input("Voulez vous : 1 Créer un Serveur / 2 Se connecter à un serveur : "))

if choix==1:

   usr=input("Rentrer votre nom d'utilisateur : ")

   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(('google.com', 0))
 
   print("Récupération de votre adresse IP...")
   time.sleep(3)
   ip=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ip.connect(("8.8.8.8", 80))
   hote=(ip.getsockname()[0])
   print("Votre IP est : "+hote)
   time.sleep(2)
   port = int(input("Rentrer le port que vous soyuhaitez utiliser : "))#on définit le port où le serveur écoute
 
   connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connexion_principale.bind((hote, port))
   connexion_principale.listen(5)
   print("Votre IP est "+s.getsockname()[0])
   print("Le serveur écoute à présent sur le port {}".format(port))
 
   connexion_avec_client, infos_connexion = connexion_principale.accept()
 
   msg_recu = b""
   #msg_recu est un binaire car les ordinateurs communiquent en binaire
 
   while msg_recu != b"fin":
       msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # réceptionné comporte des caractères spéciaux hors ASCII car il
    # faudrait définir le format de décodage
       print(msg_recu.decode())
    
       message_a_envoyer=usr+" > "+input(usr+" > ")
       message_reponse=message_a_envoyer.encode()
       connexion_avec_client.send(message_reponse)
 
   print("Fermeture de la connexion")
   connexion_avec_client.close()
   connexion_principale.close()


if choix==2 :
   usr=input("Entrer votre nom d'utilisateur : ")
 
   hote = input("Rentrer l'IP du serveur : ") #127.0.0.1 est l'ordinateur lui-même : localhost
# Mettre ici l'adresse IP du serveur s'il est sur un autre ordinateur
   port = int(input("Rentrer le port utilisé : ")) #le port de communication avec le serveur
 
   connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connexion_avec_serveur.connect((hote, port))
   print("Connexion établie avec le serveur sur le port {}".format(port))
 
   msg_a_envoyer = b""
   while msg_a_envoyer != b"fin":
       msg_a_envoyer= usr+" > "+input(usr+" > ")
    # L'instruction ci-dessous peut lever une exception si le message
    # réceptionné comporte des caractères spéciaux hors ASCII car il
    # faudrait définir le format d'encodage
       msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
       connexion_avec_serveur.send(msg_a_envoyer)
       msg_recu = connexion_avec_serveur.recv(1024)
       print(msg_recu.decode()) # même remarque que si dessus
 
   print("Fermeture de la connexion")
   connexion_avec_serveur.close()
