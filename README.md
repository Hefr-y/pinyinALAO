# **[pinyinALAO](https://github.com/Hefr-y/pinyinALAO)**
  

![banner](https://github.com/Hefr-y/pinyinALAO/blob/main/pinyinALAO/static/styles/homestyle/images/logo.png)

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Hefr-y/pinyinALAO/blob/main/LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Exercice de pinyin et recherche de pinyin pour les caractères chinois, corpus de vocabulaire chinois du HSK. Peut être utilisé pour aider à l'apprentissage des caractères chinois et à la préparation des examens du HSK. Dans le cadre d'un projet de cours [TAL et apprentissage des langues](https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/master-XB/master-sciences-du-langage-IBC7OSQ4/parcours-industrie-de-la-langue-IBC7YS7U/ue-defis-du-tal-KN02KC91/tal-et-apprentissage-des-langues-KN02POEH.html).

Basé sur le développement de [pypinyin](https://github.com/mozillazg/python-pinyin) et [Django](https://www.djangoproject.com/).

- Rapport sur ce projet : https://wiki.lezinter.net/_/Projets:Projet_NiHao!_HanZi
- GitHub : https://github.com/Hefr-y/pinyinALAO
- Python version : 3.8

## Table des matières

- [Caractéristiques](#caractéristiques)
- [Contexte](#contexte)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)

## Caractéristiques

- Recherche du pinyin.
- Séparation du front-end et du back-end ( [Django](https://www.djangoproject.com/) ).
- E-learning du pinyin en fonction des niveaux de vocabulaire du HSK.
- Évaluer la similarité des réponses et des corrigés.

## Contexte

Voir le rapport détaillé de ce projet sur notre site de [Wiki : GBLL, TAL, ALAO, etc.](https://wiki.lezinter.net/_/Projets:Projet_NiHao!_HanZi).

## Installation

Cloner le projet depuis notre site Github : 
```bash
$ git clone https://github.com/Hefr-y/pinyinALAO.git
```

Ce projet utilise [Django](https://www.djangoproject.com/) et [pypinyin](https://github.com/mozillazg/python-pinyin). Allez les voir si vous ne les avez pas installés localement :

```bash
$ pip install Django
```

```bash
$ pip install pypinyin
```

### Méthode d'installation recommandée

> 
> Afin de ne pas polluer l'environnement de votre répertoire de travail actuel, nous vous recommandons d'installer toutes les dépendances de ce projet via [pipenv](https://github.com/pypa/pipenv).

Cloner le projet depuis notre site Github : 

```bash
$ git clone https://github.com/Hefr-y/pinyinALAO.git
```

**[Pipenv](https://github.com/pypa/pipenv) peut être installé avec Python 3.6 et plus.**

Si vous utilisez Debian Buster+ 

```bash
$ sudo apt install pipenv
```
    
Ou, si vous utilisez Windows :

```bash
$ pip install --user pipenv
```

Sinon, consultez la [documentation de pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) pour obtenir des instructions.


Ensuite, sous le répertoire générale du projet où se trouvent les fichiers ***Pipfile*** et ***Pipfile.lock***

```bash
$ pipenv install
```

✨🍰✨


## Usage
Pour lancer la procédure, suivez les étapes suivantes:
1. Démarrer l'environnement virtuel
```bash
$ pipenv shell
```

2. Aller dans le répertoire du projet via ***cd*** (Ex:si le projet est dans ***Desktop***)
```bash
$ cd Desktop
```

3. Accéder au projet via le ***cd Nom_du_Projet*** où se trouvent le fichier ***manage.py*** (Ex:si le projet est ***pinyinALAO***)
```bash
$ cd pinyinALAO
```

4. Démarrage
```bash
$ python manage.py runserver
```
Le serveur local devrait ainsi se lancer à l'adresse **http://127.0.0.1:8000/** ou **localhost:8000**

**Note:**<br>

Si votre ordinateur est sous `windows`, nous vous recommandons d'utiliser un navigateur ***IE (Internet Explorer Edge)*** pour accéder aux pages afin d'assurer un affichage correct du CSS.

## API principale

**get_py_details( *hans* )**

​	*obtenir des informations correctes sur un pinyin*

**Args** :	

-  *hans* ( chaîne unicode ou liste de chaînes de caractères ) Chaînes de caractères chinoises

**Returns** : Informations sur le pinyin

**Type de Returns** : dict

------

**get_shengmu( *pinyin* )** <br>
**get_tone( *pinyin* )**

**Args** :	

-  *pinyin* ( chaînes de caractères ) L'entrée pinyin par l'utilisateur

**Returns** : <br>
          L'initiale de l'entrée pinyin <br>
          La partie du ton du pinyin (chiffre)

**Type de Returns** :<br> 
          str <br>
          digit

------

**get_yunmu( _pinyin,shengmu_ )**

**Args** :	<br>

-  *pinyin* ( chaînes de caractères ) l'entrée pinyin par l'utilisateur
-  *shengmu* ( chaînes de caractères ) la partie d'initiale du pinyin

**Returns** : <br> 
la partie de finale du pinyin

**Type de Returns** :<br>
str

------

**Levenshtein_Distance( _str1,str2_ )**

​	*obtenir des informations correctes sur un pinyin*

**Args** :	

-  *str1* ( chaînes de caractères ) N'importe quelle chaîne
-  *str2* ( chaînes de caractères ) N'importe quelle chaîne

**Returns** : <br> 
similarité des chaînes.

**Type de Returns** :<br>
float

## Pistes d'amélioration futures

- [ ] Soumettre les TODO aux [issues de Github](https://github.com/Hefr-y/pinyinALAO/issues)
- [ ] Optimisation UI
- [ ] Sauvegarde des informations sur le pinyin des caractères chinois dans une base de données
- [ ] Explications en langue étrangère du vocabulaire du HSK
- [ ] Déploiement des projets sur le serveur
- [ ] Ajouter des traits aux caractères chinois
- [ ] ...

