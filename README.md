Projet Centrale d'échecs

PARTIE I. Préparer votre machine

Note: Si vous avez déjà effectué les étapes 1 et 2 et que vous n’avez ni modifié ni supprimé des éléments du programme, vous pouvez commencer à l’étape 3 directement.

Etape 1 - Récupération du code sur votre ordinateur

Créer un dossier cible sur votre machine dans lequel le programme sera récupéré. Le nom du dossier doit de préférence être simple. Exemple : “web_scrapper”.
Ouvrir un terminal (Cygwin par exemple).
Utiliser la commande suivante pour aller dans le dossier cible :

    cd <chemin vers le dossier>

Copier le lien vers le dépôt GitHub du projet : https://github.com/FlorianRyda/P4_florian_dalloz.git
Cloner le dépôt Github en local pour pouvoir exécuter le programme sur ordinateur en tapant la commande suivante puis en la validant dans le terminal :

    git clone git@github.com:FlorianRyda/P4_florian_dalloz.git  

Le programme devrait à présent être cloné dans le dossier cible que vous avez créé.
Cette étape n’aura pas besoin d’être répétée tant que le dépôt cloné ne sera pas modifié ou supprimé de votre machine.

Etape 2 - Créer l’environnement virtuel

Utilisez la commande python --version dans votre terminal pour vérifier que la version de Python est 3.3 ou ultérieure.
Si ce n’est pas le cas, il faudra réinstaller Python depuis https://www.python.org/downloads/.
A présent il faut activer l’environnement virtuel avec le commande suivante dans le terminal :

    python -m venv env

Un dossier “env” est à présent créé dans le dossier cible. 
Cette étape n’aura pas besoin d’être répétée tant que le dépôt cloné ne sera pas modifié ou supprimé de votre machine.

Etape 3 - Activer l’environnement virtuel

Cette procédure dépend du système d’exploitation utilisé.
Sous MacOS/ Linux

Taper et valider dans le terminal :

Sous Mac

    source env/bin/activate  

Sous Windows

Taper et valider dans le terminal : env/Scripts/activate.bat
Alternative pour Windows - Sous ma version de Windows 10 cette commande ne fonctionnait pas et j’ai plutôt utilisé la succession suivante :

-Utiliser la commande cd pour aller dans le dossier “env”
-Taper et valider dans le terminal :

    source ./Scripts/activate  

-Utiliser ensuite la commande (deux fois):

    cd ..  

Cela vous permet de remonter ensuite dans l'aborescence et exécuter correctement le programme (vous devez être au niveau de le dossier chess_tournament)

Quelle que soit la commande utilisée, le nom de l’environnement apparaîtra entre parenthèses au début de chaque ligne du terminal.

Dans le cas présent, ce sera :(env)

Etape 4 - Importer les paquets

Cette étape permet d’installer tous les modules nécessaires à l’exécution du programme.
Notez qu'une fois que vous aurez effectuer cette opération une première fois, vous n'aurez pas besoin de l'effectuer à nouveau.

Tapez et valider dans le terminal :

    pip install -r requirements.txt  

Tapez et valider dans le terminal :

    pip freeze  

Une liste de modules apparaît et elle devrait au moins contenir tous les modules se trouvant dans le fichier “requirements.txt”.

Etape 5 (Optionnelle)

Cette étape n'est pas nécessaire pour l'exécution du programme. Elle vous sert uniquement à générer un rapport flake-8.

Une fois dans le dossier du programme et l'environnement virtuel activé, tapez la commande dans le terminal: 

   pip install flake8-html  
    
Cela va installer le paquet nécessaire à la création du rapport. Ensuite, tapez : 

    flake8 --format=html --htmldir=flake-report

un dossier va apparaitre dans le repository, vous pouvez alors le consulter

Then run flake8 passing the --format=html option and a --htmldir:

$ flake8 --format=html --htmldir=flake-report




 

PARTIE II. Exécution du programme

Voici l’étape la plus attendue, il est temps de lancer ce programme !

Taper et valider dans le terminal :

    python -m chess_tournament. 

Tout ce programme fonctionne via le terminal. Les commandes possibles vous seront toujours affichées à l'écran, il vous suffira de taper la lettre ou le chiffre correspondant puis de valider en tapant sur la touche "Entrée". 

ATTENTION : ne faites pas usage des accents, le programme n'est pas en mesure de les interpréter.

Sauvergarde des données : Lorsque vous créez/modifiez ou supprimez un tournoi/joueur, toutes les données sont sauvegardées dans un fichier json "database.json".

Cela vous permet d'assurer la permanence de ces données. Ne quittez pas le programme "de force" pendant que vous créez/modifiez/supprimez ET que le programme n'affiche pas clairement que vous pouvez le quitter via une commande car les modifications apportées pourraient ne pas être prises en compte.

Un premier écran va apparaitre pour vous donner le choix entre: 
La gestion des joueurs (indépendament des tournois)
La gestion des tournois
Quitter le programme (cette option sera par la suite toujours disponible)

1) La Gestion des Joueurs

Cette partie vous permet : 
-De consulter les détails d'un joueur,
-D'ajouter un joueur,
-De supprimer un joueur,
-De modifier le classement d'un joueur,
-Revenir à la page d'accueil.

2) La gestion des tournois

Cette partie vous permet :

A) De consulter tout tournoi passé ou en cours,

Vous arrivez alors sur la page de détails du tournoi.

Si le tournoi n'est pas encore terminé:

Vous allez ensuite créer chaque round un par un. Le premier sera créé via la touche "C" et chaque suivant avec la touche "S". 
Une fois le round créé, vous pourrez sélectionner et entrer le résultat de chaque match. Vous pourrez sélectionner les matchs dans l'ordre que vous souhaitez.

Une fois tous les rounds terminés, vous pourrez modifier le classement des joueurs. 
Vous pouvez à tout moment trier les joueurs par ordre alphabétique ou par classement.
 
B) De créer un nouveau tournoi,

Lors de la création d'un tournoi:

Vous allez entrer les information du tournoi
Vous allez sélectionner les 8 joueurs que vous devez ajouter au tournoi. Vous ne pourrez pas quitter le programme à ce stade via une commande. 
Si vous avez moins de 8 joueurs enregistrés, vous serez redirigé sur la page de création de joueurs.

Vous arrivez alors sur la page de détails du tournoi.

Vous allez ensuite créer chaque round un par un. Le premier sera créé via la touche "C" et chaque suivant avec la touche "S" 

Une fois le round créé, vous pourrez sélectionner et entrer le résultat de chaque match. Vous pourrez sélectionner les matchs dans l'ordre que vous souhaitez.

Une fois tous les rounds terminés, vous pourrez modifier le classement des joueurs. 

Vous pouvez à tout moment trier les joueurs par ordre alphabétique ou par classement.

Un message sera affiché ("Tournoi Terminé !") sur la page de détails du tournoi lorsque celui-ci est terminé.

C) Modifier les informations d'un tournoi,
D) Revenir à la page d'accueil.

Bonne utilisation !

 