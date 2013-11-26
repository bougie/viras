### VIRAS: Virtual Appartland Services

VIRAS vous permet de gerer differentes VMs qui tournent sur vos differentes machines physiques.

A term, il supportera :

* Xen
* KVM
* LXC
* Zones solaris
* Jails BSD


### Technologie

* Django
* Fabric
* MySQL ou SQLite


Viras est conçu selon une architecture REST + JSON. Il respect les codes retour du protocole HTTP ainsi que les methodes de requetes.
Ainsi, on aura comme methodes :

* GET pour recuperer les informations
* POST pour ajouter un element
* PUT pour modifier un element
* DELETE pour supprimer un element


### Terminologie

* compute : hote physique sur lequel tourne une technologie de virtualisation
* instance : machine virtuelle (indépendamment de la technologie de virtualisation)
* flavour : model d'instance
* keystore : clef SSH pour se connecter aux instances

### Authentification

3 variables permettent d'identifier et d'authentifier l'utilisateur :

* api_key
* api_secret
* consumer_key

Les variables **api_key** et **api_secret** permettent d'identifier et d'authentifier l'application qui utilise l'API (un script, une IHM, etc).
La variable **consumer_key** permet d'identifier l'utilisateur qui utilise l'API et ainsi d'appliquer les droits sur les ressources interogées.

Processus d'authentification
* créer "l'application" (cad le couple api_key / api_secret) s'il n'existe pas
* envois d'une requete POST sur /key/consumer contenant :
  * api_key
  * api_secret
  * login
  * mot de passe
* le serveur repond en envoyant le token de connexion **consumer_key**

Pour l'acces aux ressources, il faut pour chaque requetes :
* envoyer la variable **api_key**
* envoyer la variable **consumer_key**
* signer la somme de toutes les variables avec le token **consumer_key**
