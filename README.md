# TBA

Ce repo contient la première version (minimale) du jeu d’aventure TBA.

Les lieux sont au nombre de 6. Il n'y a pas encore d’objets ni de personnages autres que le joueur et très peu d’interactions. Cette première version sert de base à ce qui va suivre, et sera améliorée au fur et à mesure.


## Structuration

Il y a pour le moment 5 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre .
