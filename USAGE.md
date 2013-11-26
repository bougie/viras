### VIRAS API - Usage

### Authentification

* POST /auth
  * api_key
  * api_secret
  * login
  * password


### Compute

* GET /compute : lister tous les computes
* POST /compute : creer un compute
  * name : nom du compute
  * vcpu : nombre de CPU
  * memory : taille de la RAm en Mo
  * disk : taille du disque dur en Go
  * ctype : technologie de virtualisation (xen, jails, zone, vmware)


* GET /compute/{compute_name} : afficher un compute
* PUT /compute/{compute_name} : editer un compute 
* DELETE /compute/{compute_name} : supprimer un compute


### Flavour

* GET /flavour : lister tous les flavours
* POST /flavour : creer un flavour
  * name : nom du flavour
  * vcpu : nombre de CPU
  * memory : taille de la RAm en Mo
  * disk : taille du disque dur en Go


* GET /flavour/{flavour_name} : afficher un flavour
* PUT /flavour/{flavour_name} : editer un flavour
* DELETE /flavour/{flavour_name} : supprimer un flavour


### Instance

* GET /compute/{compute_name}/instance : lister les instance d'un compute
* POST /compute/{compute_name}/instance : creer une instance
  * name : nom de l'instance
  * desc : description de l'instance
  * flavour : nom de la flavour utilisée comme modele


* GET /compute/{compute_name}/instance/{instance_name} : afficher une instance
* PUT /compute/{compute_name}/instance/{instance_name} : editer la description d'une instance

### Keystore

* GET /key/api : lister toutes les applications
* POST /key/api : creer un compute
  * name : nom de l'application
  * description : description de l'application


* GET /key/api/{api_id} : afficher une application
* DELETE /key/api/{api_id} : supprimer une application


* GET /key/consumer : lister tous les tokens


* GET /key/consumer/{consumer_id} : afficher un token
* DELETE /key/consumer/{consumer_id} : supprimer un token
