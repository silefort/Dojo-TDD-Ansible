# Dojo TDD Ansible

L'objectif de ce Dojo est de démontrer l'utilisation que l'on peut faire d'Ansible et comment on peut mettre en pratique les bonnes pratiques de développement logiciel sur des projets d' Infrastructure As Code

## Principes de base et pré-requis :

### Arborescence de départ :

```
deployer.py => Outil en ligne de commande permettant d'utiliser les principales commandes du Dojo
docker-compose.yml => Fichier Docker-compose permettant de déployer l'environnement de test des playbooks Ansible
```

## Déroulé

### Lancer l'environnement du Dojo

```
$ ./deployer.py run -b -n
```

## Requirements

* docker doit être installé (`docker --version` pour vérifier)
* python3 doit être installé (`python --version` pour vérifier)
* pytest doit être installé (`pytest --version` pour vérifier)
