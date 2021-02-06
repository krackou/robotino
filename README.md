# Robotino

## Description

projet d'édition collaborative d'un robot adapté au réseau Discord, et servant des initiatives anarchistes.

 - Action de display des infos comme encyclopédie, météo, actualités, statistiques, formules, data diverses
 - Pouvoir gérer les membres et les rôles, expulser/muter
 - Gérer l’accueil : poser questions et passer membre
 - Gérer des jeux
 - IA de conversation

## Installation

Requiert `python >= 3.5.3`

Il est nécessaire d'avoir crée une [Application Discord](https://discord.com/developers/applications).
Ainsi que de pouvoir s'authentifier a l'[API de Reddit](https://www.reddit.com/wiki/api)

### Debian

Avant toute chose, il est fortement conseillé de préparer un environnement virtuel python sur votre machine.
Cela permet un meilleur contrôle de l'environnement, de mieux gérer le versionnage des dependances
si d'autres projets peuvent tourner sur la même machine, ainsi que de palier a des éventuels failles
de sécurité.

Voir la documentation de [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) pour plus d'informations.

Ensuite sauvegardez les identifiants Discord et Reddit dans votre environnement virtuel.

Un moyen de faire ca de manière durable est d'éditer le fichier `~/.bashrc` avec les lignes suivantes:
```bash
# Discord bot env variables
export REDDIT_SECRET={your_reddit_secret}
export REDDIT_ID={your_reddit_id}
export DISCORD_TOKEN={your_discord_token}
```

Puis exécuter les commandes :
```bash
source ~/.bashrc;
workon {your_virtualenv};
```

Une fois ces etapes terminees, il est simple d'installer le project.
Allez dans votre terminal et entrez les commandes suivantes :

```bash
cd ~;
git clone https://github.com/krackou/robotino;
cd ./robotino;
pip install . -r dev-requirements.txt;
```

Et voilà, le Bot est installé !

## Usage

Une fois le bot installé, vous pouvez le lancer à tout moment avec la commande :
```bash
python -m robotino;
```

N'oubliez pas d'activer votre environnement virtuel pour que cette commande marche ;)