### VIRAS API - Usage

### Compute

* GET /compute : lister tous les computes
* POST /compute : creer un compute
  * name : nom du compute
  * vcpu : nom de CPU
  * memory : taille de la RAm en Mo
  * disk : taille du disque dur en Go
  * ctype : technologie de virtualisation (xen, jails, zone, vmware)


* GET /compute/{compute_name} : afficher un compute
* PUT /compute/{compute_name} : editer un compute 
* DELETE /compute/{compute_name} : supprimer un compute
