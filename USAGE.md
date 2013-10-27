### VIRAS API - Usage

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

* POST /compute/{compute_name}/instance : creer une instance
  * name : nom de l'instance
  * desc : description de l'instance
  * flavour : nom de la flavour utilisée comme modele

