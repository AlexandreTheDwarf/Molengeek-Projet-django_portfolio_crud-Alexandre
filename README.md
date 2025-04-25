# Molengeek Projet Django Portfolio CRUD - Alexandre

## Description

Ce projet est une application Django de gestion de portfolio, permettant la gestion des catégories et des éléments de portfolio via une interface d'administration personnalisée. L'application offre un CRUD complet pour les catégories de portfolio et les éléments associés, y compris l'upload d'images pour chaque élément de portfolio.

Les principales fonctionnalités sont :
- Création, lecture, mise à jour et suppression de catégories de portfolio.
- Création, lecture, mise à jour et suppression d'éléments de portfolio.
- Association d'images à des éléments de portfolio.
- Interface d'administration personnalisée avec Bootstrap.

## Fonctionnalités

- **Gestion des catégories de portfolio** : Ajouter, modifier, supprimer des catégories de portfolio.
- **Gestion des éléments de portfolio** : Ajouter, modifier, supprimer des projets avec des descriptions, des dates de projet, des liens et des images associées.
- **Upload d'images** : Chaque projet de portfolio peut être accompagné de plusieurs images.
- **Interface d'administration** : Interface d'administration personnalisée avec des formulaires bootstrap et un affichage en cartes des éléments de portfolio.

## Prérequis

Assurez-vous d'avoir installé les éléments suivants pour pouvoir exécuter ce projet :

- **Python 3.x**
- **Django 4.x**
- **Pillow** (pour la gestion des images)
- **crispy-forms** (pour une meilleure présentation des formulaires)
- **SQLite** ou une autre base de données relationnelle supportée par Django

## Installation

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/ton_utilisateur/Molengeek-Projet-django_portfolio_crud-Alexandre.git
   cd Molengeek-Projet-django_portfolio_crud-Alexandre
   ```

2. **Créer un environnement virtuel et l'activer :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations de base de données :**

   ```bash
   python manage.py migrate
   ```

5. **Créer un super utilisateur (facultatif mais recommandé pour accéder à l'interface d'administration) :**

   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur de développement :**

   ```bash
   python manage.py runserver
   ```

7. **Accéder au projet dans votre navigateur :**

   Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/` pour voir le projet.

   L'interface d'administration est accessible à `http://127.0.0.1:8000/admin/`. Connectez-vous avec le compte super utilisateur que vous avez créé précédemment.

## Structure du projet

```plaintext
Molengeek-Projet-django_portfolio_crud-Alexandre/
├── adminSide/                   # Contient l'interface d'administration personnalisée
│   ├── templates/
│   │   └── adminSide/
│   │       └── ...              # Templates HTML pour l'interface d'administration
│   ├── views.py                 # Vues pour gérer l'interface d'administration
│   ├── forms.py                 # Formulaires pour créer/mettre à jour les éléments
│   └── models.py                # Modèles pour PortfolioCategory, PortfolioItem, PortfolioImage
├── portfolio/                   # Application principale du portfolio
│   ├── templates/
│   │   └── portfolio_details.html  # Template pour afficher un élément de portfolio
│   ├── views.py                 # Vues pour afficher le portfolio
│   ├── models.py                # Modèles pour PortfolioCategory, PortfolioItem, PortfolioImage
│   └── forms.py                 # Formulaires pour ajouter des projets
├── media/                       # Dossier pour stocker les images téléchargées
├── static/                      # Dossier pour les fichiers statiques (CSS, JS, images)
├── manage.py                    # Fichier pour interagir avec Django
└── requirements.txt             # Liste des dépendances du projet
```

## Utilisation

1. **Page d'administration** : Vous pouvez gérer vos éléments de portfolio et catégories à travers l'interface d'administration Django (`/admin`).
2. **Page du portfolio** : Les éléments de portfolio sont affichés sur une page publique, et vous pouvez ajouter des projets via l'interface d'administration.
3. **Ajout d'images** : Pour chaque élément de portfolio, vous pouvez télécharger des images associées.

## Développement

### Ajouter un élément de portfolio

1. Allez dans l'interface d'administration (`/admin`).
2. Allez dans "Portfolio" > "Portfolio Items" et cliquez sur "Add Portfolio Item".
3. Remplissez les champs : titre, client, description, date, URL du projet et téléchargez une image si nécessaire.

### Ajouter une catégorie de portfolio

1. Allez dans "Portfolio" > "Portfolio Categories" et cliquez sur "Add Portfolio Category".
2. Donnez un nom à la catégorie et sauvegardez.

### Affichage des projets

Les projets seront affichés avec une carte contenant les informations principales, y compris une image si elle est téléchargée.

