# <span style="color:  #3b43ee  ">Création de trame d'un dossier:</span>

_Ce script fonctionne sous python 3 ==>_ <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=50 align=center>

_Il a pour but de faciliter la réception de dossiers en créant une trame d'arborescece et en fournirssant les principaux documents nécessaires._

<span style="color:  #3b43ee  ">1.</span> L'utilisateur entre le nom de son dossier ou le numéro de sa procédure _(le cas échant il remplace les "/" par des "-")_.

<span style="color:  #3b43ee  ">2.</span> Il choisit l'emplacement où il souhaite créer son nouveau dossier. _(plusieurs dossiers peuvent être crées à la suite)_

## <span style="color: #ee643b ">Liste des commandes à exécuter pour lancer le programme:</span>

_Pré-requis: se placer depuis le terminal, dans le dossier où l'on exécute le script:_

Avant toute chose on clone le répository git:

```bash
git clone https://github.com/LGD-P/Gestion_arboresences_dossiers.git
```
On créer l'environnement virutel:

```bash
python3 -m venv env
```

Puis on lance l'installation des modules nécessaires au fonctionnement du script:

```bash
pip install -r requirements.txt
```

Une fois les modules installés on active l'environnement virutel:

```bash
source env/Scripts/Activate
```

Il n'y a plus qu'à exécuter le script:

```bash
python creation_dun_nouveau_dossier.py
```

<span style="color:  #ee643b  ">Note:</span>

Le répertoire _"fond de dossier"_ peut être modifié en fonction des besoins de l'utilisateur et des fichiers ou sous-dossiers peuvent être ajoutés ou enlevés. Ils seront automatiquement pris en compte, dans la création du nouveau dossier.
