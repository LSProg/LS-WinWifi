 # LS-WinWifi
***
### Description:
LS-WinWifi est un programme de gestion des profils wifi dans un environement Windows.
Il permet l'exportation et l'importation d'un ou plusieurs profils wifi à l'aide d'une simple commande shell.
***
## Utilisation
Ouvrez un terminal CMD et entrez :
```
      CD /d "Rerpertoire de l'executable/script"
```
Pour afficher l'aide du programme vous pouvez exécuter 
```
      LS-WinWifi.exe
```
Pour fonctionner le programme doit etre executer avec des arguments:
```
      LS-WinWifi.exe i[Arg1] [Arg2]
```
Exemple 1 :
```
      LS-WinWifi.exe import all
```
Exemple 2 :
```
      LS-WinWifi.exe export "my wifi ssid"
```
voici la liste complète des arguments :
```yaml 
        [Arg1]
              export: Permets de définir le mode exportation des profils
                      le programme va exporter le/les profil(s) au format XML
              import: permets de définir le mode importation des profils
                      si le dossier contenant les fichiers XML existe, le
                      programme va importer le/les profil(s)
        [Arg2]
              All : va appliquer la méthode fournie dans l'argument 1 à l'essemble des profils.
              "nom du profile" : va rechercher le nom du profil et appliquer la méthode fournie
                                 dans l'argument 1 si l'action est possible (importation, fichier XML existant)
                                  
```

***
### Licence : Creative Commons CC BY-NC-SA 4.0 [disponible ici](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr) 
***
### Code Source [ici](LS-WinWIFI.py) 
