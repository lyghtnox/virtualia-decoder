# virtualia-decoder
Code python pour déchiffrer les identifiants transmis par virtualia sur le réseau

## Pourquoi?
[Virtualia](https://www.virtualia.fr/) chiffre les identifiants transmis sur le réseau entre les clients et le serveur.
Certains pourraient penser que ce chiffrement est suffisant pour assurer la sécurité des utilisateurs.
Ce code prouve que ce n'est pas le cas et qu'un chiffrement asymétrique (tel que TLS) est nécéssaire.

## Installation
```
git clone https://github.com/lyghtnox/virtualia-decoder
pip install -r requirements.txt
```

## Utilisation
Pour déchiffrer un mot de passe chiffré:
```
python3 decode.py <chaine chiffrée>
```

Pour parse un fichier .pcap et déchiffrer les mots de passe virtualia capturés:
```
python3 pcap_parser.py capture.pcap
```
