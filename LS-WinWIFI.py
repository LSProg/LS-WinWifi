__author__ = "LS_Prog"
__copyright__ = "Copyright (C) 2022 LS_Prog"
__license__ = "Licence Creative Commons CC BY-NC-SA 4.0"
__version__ = "0.1"
__contact__ = "logan.s.prog@gmail.com"
__nom_programme__ = "LS_WinWifi"


import os, time, art
from sys import argv
from colorama import init,Fore,Back,Style
from random import randint, choice
from art import text2art
init(autoreset=True)#for colorama

COULEUR = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
INDEX_COULEUR = {"vert":0,"rouge":1,"jaune":2,"bleu":3,"magenta":4,"cyan":5}
SYMBOL_AFFICHAGE = ['#','-','=','*']
LIGNE_TEXTE_INTRO_0 = """Ce programme est mis à disposition selon les termes de la Licence Creative Commons,
Attribution - Pas d'Utilisation Commerciale - Pas de Modifications 4.0 International.
plus de details:
http://creativecommons.org/licenses/by-nc-nd/4.0/"""

#constantes programme
NOM_UTILISATEUR = os.environ["USERNAME"]
PROFILE = os.environ['USERPROFILE']
DOSSIER = "{}\WiFi {}".format(PROFILE,NOM_UTILISATEUR)
COMMANDE2 = 'mkdir "{}"'.format(DOSSIER)

INVITE_1 = "Appuyez sur entrer pour continuer"
INVITE_2 = "Remarque: si vous continuez vous acceptez les termes de la licence"
INVITE_3 = "Lecture du fichier temporaire ..."
INVITE_4 = "Extraction du profil: "
INVITE_5 = "\nNettoyage des fichiers temp en cours veuillez patienter ..."
INVITE_6 = "Job terminé !"
INVITE_7 = "Appuyez sur entrer pour terminer !\n>>>"
INVITE_8 = "Génération du fichier XML pour le profil: "
INVITE_9 = "Appuyez sur entrer pour terminé ce programme"
INVITE_ERREUR = "les service wlansvc n'est pas activer, la cause la plus probable est une abscence de carte wifi ou probleme de pilote."

ASCI_NOM_PROG = text2art(__nom_programme__,"random")

#Fonctions
Passe_Ligne = lambda: print("\n")

def Cmd(commande):
    """ execute une commande est renvoie le resultat de cette commande
    """
    stream = os.popen(commande)
    output = stream.read()
    return output
    
def Clear():
    """ nettoie le shell """
    try:
        os.system("cls")
    except:
        print("\n\n\n")

def Check_Path(path,create=False):
    """ verifie si le repertoire spécifier existe """
    resultat = os.path.exists(path)
    if not resultat:
        if create:
            os.mkdir(path)
            resultat = True
    return resultat 
        
def Pause(invite=INVITE_1):
    """ met le programme en pause, jusqu'a ce que l'utilisateur appuie sur entrer """
    Affichage_Couleur(invite,"jaune")
    input()
    
    
def listdirectory(path):
    """ source : https://python.developpez.com/faq/?page=Fichier
    va recuperer les nom des fichiers dans un repertoire et les renvoyer sous forme de liste """
    fichier=[]
    for root, dirs, files in os.walk(path):
        for i in files:
            fichier.append(i)
    return fichier


def Affichage_Couleur(invite1,couleur1="vert",invite2=None,couleur2="vert",pause=False):
    """ permet d'afficher des information en couleur dans le shell """
    invite1 = str(invite1)
    invite2 = str(invite2)
    if invite2 != "None":
        print((COULEUR[INDEX_COULEUR[couleur1]] + invite1) + (COULEUR[INDEX_COULEUR[couleur2]] + invite2))
    else:
        print((COULEUR[INDEX_COULEUR[couleur1]] + invite1))
    if pause:
        Pause()


def Cadre(invite,caractere="-",largeur=80,couleur_tiret="bleu",couleur_msg="jaune",pause=False):
    """ permet de faire un cadre en ASCI dans le shell """
    tiret = f"{caractere}".center(largeur,caractere)
    Affichage_Couleur(tiret,couleur_tiret)
    if type(invite) == list:
        for i in invite:
            i = str(i)
            Affichage_Couleur(i,couleur_msg)
    else:
        Affichage_Couleur(invite,couleur_msg)
    Affichage_Couleur(tiret,couleur_tiret)
    print("\n\n")
    if pause:
        Pause()

def Affichage_Asci():
    """ permet de faire une baniére du nom du programme dans le shell """
    Clear()
    print(ASCI_NOM_PROG)

    
def Affichage_Licence():
    """ permet de faire accepter la licence a l'utilisateur du programme """
    liste=[]
    liste.append(LIGNE_TEXTE_INTRO_0)
    liste.append(LIGNE_TEXTE_INTRO_1)
    liste.append(LIGNE_TEXTE_INTRO_2)
    liste.append(LIGNE_TEXTE_INTRO_3)
    Cadre(liste)
    Affichage_Couleur(INVITE_1,"jaune")
    Affichage_Couleur(INVITE_2,"rouge")
    input()



        

##Class
class Profile:
    """ classe qui va servire de support au profile WIFI """
    def __init__(self, name,rep=None):
        self.name = name
        self.repertoire = rep
        
    def Gen_XML(self):
        Affichage_Couleur(INVITE_8,"jaune",self.name,"bleu")
        Check_Path(DOSSIER,True)
        commande = 'netsh wlan export profile "{}" key=clear folder="{}"'.format(self.name,DOSSIER)
        Cmd(commande)

    def importation(self):
        Affichage_Couleur("Importation du profile : ","jaune",self.name,"bleu")
        os.system(f'netsh wlan add profile filename="{self.repertoire}" user=all')
       



        
class Programme:
    """ classe qui sert de coeur au programme """
    def __init__(self):
        self.en_cour = True
        self.arguments = argv
        self.profiles = []

    def Help(self):
        """ fonction qui permet d'afficher de l'aidde sur l'utilisation du prgramme dans le shell """
        Affichage_Couleur("Executer ce script dans un terminal CMD.","jaune")
        Affichage_Couleur("Entrer des double guillemet pour le nom du repertoire et le nom du profile","jaune")
        Affichage_Couleur("Utilisation:\npython [REPERTOIRE] [import/export] [all/profile_name]\n ","jaune")
        Affichage_Couleur('Exemple 1: ','jaune','LS-WinWifi.exe "C:\path\script.py" export all',"bleu")
        Affichage_Couleur('Exemple 2: ','jaune','LS-WinWifi.exe "C:\path\script.py" import "my_wifi_name"',"bleu")
        Affichage_Couleur('Exemple 3: ','jaune','LS-WinWifi.exe "C:\path\script.py" import all',"bleu")
        Affichage_Couleur('Exemple 1: ','jaune','LS-WinWifi.exe "C:\path\script.py" export "my wifi name"',"bleu")
        
    def Import(self,arg):
        """ fonction qui va importer selon les argument un ou plusieur profile wifi """
        Affichage_Asci()
        resultat = Check_Path(DOSSIER)
        if resultat:
            liste = listdirectory(DOSSIER)
            liste2 = []
            Cadre("recherche de fichier XML ...")        
            for i in liste:
                j = i.split(".")
                j = j[1]
                if j.find("xml") == 0:
                    fichier = f"FICHIER:{i}"
                    Affichage_Couleur("fichier XML trouver :", "bleu",fichier,"vert")
                    print("")
                    rep = f"{DOSSIER}\\{i}"
                    liste2.append(Profile(i,rep))
            for instance in liste2:
                if arg == "all" or arg == instance.name:
                    instance.importation()

            Affichage_Couleur("Job terminé")
            time.sleep(5)
        else:
             Affichage_Couleur(f"le repertoire '{DOSSIER}' n'existe pas.\nil est impossible d'importer des profil wifi")
            
        
    def Get_Profile_Name(self):
        """ va lister les nom des profile wifi existant"""
        resultat = Cmd("netsh wlan show profile")
        lignes = resultat.split("\n")
        cptr = 0
        for i in lignes:
            liste = i.split(":")
            try:
                element = liste[1]
                if not element == " ":
                    liste2 = element.split(" ")
                    profile_name = liste2[1]
                    self.profiles.append(Profile(profile_name))
            except:
                pass
        
        
    
    def Export(self,arg):
        """ va exporter au format xml un ou plusieurs profile wifi, selon les argument fournis lors de l'execution """
        Affichage_Asci()
        self.Get_Profile_Name()
        if arg == "all":
            comfirmation = True
            for profile in self.profiles:
                profile.Gen_XML()

        else:
            comfirmation = False
            for profile in self.profiles:
                if profile.name == arg:
                    profile.Gen_XML()
                    comfirmation = True

        if comfirmation:
            os.startfile(DOSSIER)
        else:
            Affichage_Couleur(f"Erreur le profile:{arg} n'a pas été trouvé !! ","rouge")
            
            
            
        
    
    def Main(self):
        suite = True
        try:
            mode = self.arguments[1]
            mode = mode.lower()
        except:
            self.Help()
        else:
            try:
                elements = self.arguments[2]
                element = elements.lower()
                recherche = element.find("'")
                if not recherche == -1:
                    self.Help()
                    Affichage_Couleur("Erreur dans votre syntaxe veuillez mettre des double guillemets !!","rouge")
                    input("Appuyer sur entrer pour terminer")
                    suite = False
                                 
                self.elements = element
            except:
                self.elements = "all"
            if suite:                
                if mode == "import":
                    self.Import(self.elements)
                elif mode == "export":
                    self.Export(self.elements)
                elif mode == "licence":
                     Affichage_Licence()
                else:
                    self.Help()



        
if __name__== "__main__":
    prog = Programme()
    prog.Main()
