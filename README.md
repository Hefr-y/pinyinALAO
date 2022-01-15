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
- [Contributing](#contributing)
- [License](#license)

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

**Pipenv peut être installé avec Python 3.6 et plus.**

Si vous utilisez Debian Buster+ 

    sudo apt install pipenv
    
Ou, si vous utilisez Windows :

    pip install --user pipenv
    
Sinon, consultez la [documentation de pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) pour obtenir des instructions.


Ensuite, sous le répertoire générale du projet où se trouvent les fichiers ***Pipfile*** et ***Pipfile.lock***

```bash
$ pipenv install
```

✨🍰✨



### Any optional sections

## Usage

```
```

Note: The `license` badge image link at the top of this file should be updated with the correct `:user` and `:repo`.

### Any optional sections

## API

### Any optional sections

## More optional sections

## Contributing

See [the contributing file](CONTRIBUTING.md)!

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

### Any optional sections

## License

[MIT © Richard McRichface.](../LICENSE)
