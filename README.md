# Modèle de DevContainer Python

## Introduction

Ce dépôt sert de gabarit pour la création de projets Python avec un environnement de développement standardisé en utilisant DevContainer. Il inclut toutes les configurations nécessaires pour démarrer rapidement un projet Python, y compris les dépendances courantes, les configurations/extensions de l'éditeur et les outils de développement.

> **Note**: Pour commencer votre propre projet en utilisant ce gabarit, veuillez consulter la section [comment utiliser ce gabarit](./docs/comment-utiliser-gabarit.md).

## Objectif

Fournir un environnement de développement cohérent et reproductible pour les projets Python.

## Ouvrir Directement dans un DevContainer

Vous pouvez ouvrir ce projet directement dans un DevContainer dans VS Code en cliquant sur le lien ci-dessous:

[![Ouvrir dans DevContainer](https://img.shields.io/static/v1?label=Open%20in%20Dev%20%20Container&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/thalleslimasys/mcc-dashboard)

> Attention : Lors de l'utilisation du bouton, le DevContainer sera toujours ouvert sur la branche main. Soyez attentif si votre travail doit être fait dans une autre branche.

## Contenu du Gabarit

- **Dockerfile** configuré pour Python 3.x.
- **devcontainer.json** pour les paramètres spécifiques du DevContainer.
- Inclusion des dépendances de base comme `pip` et autres librairies couramment utilisées.
- Intégration avec Visual Studio Code pour une expérience de développement optimisée.
- Documentation pour l'installation et l'utilisation du DevContainer.

## Prise en Main

### Prérequis

- Docker/Rancher Desktop
- Visual Studio Code
- Extension Remote - Containers pour VS Code

## Configuration des Principaux Fichiers

### Dockerfile

Le Dockerfile configure l'image de base et installe les dépendances nécessaires pour Python.

### devcontainer.json

Le fichier `devcontainer.json` configure les paramètres spécifiques pour DevContainer, intégrant Visual Studio Code et définissant les dépendances et les extensions à installer.

### setup.py

Le fichier `setup.py` est utilisé pour configurer la distribution du package Python. Pour plus d'informations sur l'utilisation de `setuptools`, consultez
[ce lien.](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)

### settings.json

Le fichier `.vscode/settings.json` contient les configurations spécifiques à l'éditeur pour améliorer l'expérience de développement.

## Structure du Projet

Voici une vue d'ensemble de la structure du projet incluse dans ce gabarit :

``` shell
gabarit-python/
│
├── 📁.devcontainer/
│ └── 📄devcontainer.json
│
├── 📁src/
│ ├── 📄init.py
│ └── 📄main.py
│
├── 📁.github/
│ └── 📁workflows/
│     ├── 📄ci.yml
│     └── 📄python-app.yml
│
├── 📁.vscode/
│ ├── 📄settings.json
│ └── 📄extensions.json
│
├── 📁tests/
│ ├── 📄init.py
│ └── 📄test_main.py
│
├── 📄.gitignore
├── 📄README.md
├── 📄requirements.txt
├── 📄Dockerfile
└── 📄setup.py
```

## Contributions

Les contributions à ce gabarit sont les bienvenues. Veuillez soumettre des pull requests ou ouvrir des issues pour toute suggestion ou amélioration.
