Ce programme est écrit en Python et il faut avoir l'environnement Python pour le lancer.
Pour faire des essais et débugger, utiliser le script BAT sous Windows. Pour un exécution standard, le fichier OpenASCAM.py peut être lancé directement.
Regarder le fichier percage.txt, indiquant comment créer un fichier de percage. En exécutant le logiciel, le fichier GCODE est généré automatiquement avec le fichier de percage qui lui a été donné.

Avant le perçage, le Z=0 doit être défini sur la CNC comme étant le point le plus bas de perçage. Idem pour les X=0 et Y=0 qui doivent être des points hors zone de perçage, car au lancement du GCODE, la machine va mettre tous ses axes à 0 sur les contacts de fin de course, pour ensuite ajouter les offsets.