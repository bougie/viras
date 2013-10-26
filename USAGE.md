### VIRAS API - Usage

### Compute

* GET /compute : liste de tous les computes
* POST /compute : creer un compute
  * name : nom du compute
  * vcpu : nom de CPU
  * memory : taille de la RAm en G
  * disk : taille du disque dur en G
  * ctype : technologie de virtualisation (xen, jails, zone, vmware)


* GET /compute/{compute_name} : afficher les details d'un compute
* PUT /compute/{compute_name} : edition d'un compute 
* DELETE /compute/{compute_name} : suppression d'un compute
