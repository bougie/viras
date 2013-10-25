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