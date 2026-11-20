# ue19-lab-05

Petite application Python qui interroge l'API publique JokeAPI (https://v2.jokeapi.dev) et affiche une blague.

## Fonctionnalités
- Appel HTTP à JokeAPI avec la librairie `requests`
- Affichage d'une blague aléatoire (en une ou deux parties)
- Gestion des erreurs réseau

## Installation
```
pip install -r requirements.txt
```

## Lancement
```
python app.py
```

## Avec Docker
```
docker build -t ue19-lab-05 .
docker run --rm ue19-lab-05
```
