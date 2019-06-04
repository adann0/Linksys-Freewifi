#!/usr/bin/env python3
# -*- coding: utf-8 -*-

SALT1 = "***_O_O_Top_Secret_O_O_***" # Changer la valeur
SALT2 = "***_O_O_Top_Secret_O_O_***" # Changer la valeur

import sys
import os
import json
import ast
import getpass
import base64

from urllib import parse, request

import cryptography.fernet
import argon2

dir_config = os.path.expanduser("~") + "/.config/freewifi/" # dir ou sont stockes les id

"""
'''Encrypt''' data with Argon2, Base64 and Fernet
"""

def encrypt(data_bytes, password, salt):
    password_hash = argon2.argon2_hash(password=password, salt=salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    encryptor = cryptography.fernet.Fernet(encoded_hash)
    return(encryptor.encrypt(data_bytes))

"""
'''Decrypt''' data encrypted with Argon2, Base64 and Fernet    
"""

def decrypt(cipher_bytes, password, salt):
    password_hash = argon2.argon2_hash(password=password, salt=salt)
    encoded_hash = base64.urlsafe_b64encode(password_hash[:32])
    decryptor = cryptography.fernet.Fernet(encoded_hash)
    return(decryptor.decrypt(cipher_bytes))

"""
Retourne differents messages (connected, failed, ...) en fonction de l'arguments
"""

def code(argv) :
    if argv.startswith("Site accessible uniquement") :
        return("Message : Site accessible uniquement a partir d'une Freebox")
    elif argv == "Identifiant inconnu" :
        return("Message : Identifiant inconnu")
    elif argv == "</div>" :
        return("Message : Connexion au service reussi")
    else :
        return("Message : ???")

"""
Recupere les ids et rajoute un bout manquant du payload avant de le retourner a la fonction connect
"""

def get_payload() :
    while True :
        try :
            flux = open(dir_config + "payload.json", "r")
            break
        except FileNotFoundError:
            identifiants()
    raw_data = flux.read()
    json_data = ast.literal_eval(raw_data)
    decrypted = decrypt(json_data["hash"].encode("utf-8"), SALT1, SALT2).decode("utf-8")
    payload = {
        "login" : json_data["login"], 
        "password" : decrypted,
        "submit" : "Valider"
    }
    return(payload)

"""
Recupere le payload et l'envoi
"""

def connect() :
    payload = parse.urlencode(get_payload()).encode("ascii")
    req =  request.Request("https://wifi.free.fr/Auth", data=payload) # this will make the method "POST"
    try :
        auth = request.urlopen(req)
    except :
        print("Message : Pas de Connexion")
        sys.exit(1)
    msg = auth.readlines()[-11] # Le message est toujours le 11eme element en partant de la fin
    print(code(" ".join(msg.decode("utf-8").split()))) #La fonction code parse correctement les message (enleve les \n \t ect)

"""
Demande les identifiants a l'utilisateur et hash le mot de passe avant de mettre le tout dans un fichier .json
"""

def identifiants() :
    login = input("Identifiant Hotspot : ")
    password = getpass("Mot de Passe : ")
    encrypted = encrypt(password.encode("utf-8"), SALT1, SALT2).decode("utf-8")
    identifiants = {"login" : login, "hash" : encrypted}
    if not os.path.exists(dir_config) : # Verifie que le repertoire config existe
        os.makedirs(dir_config)
    with open(dir_config + "payload.json", "w") as flux:
        json.dump(identifiants, flux) # Enregistre les identifiants

if __name__ == "__main__" :
    if (len(sys.argv) == 1) or (len(sys.argv) > 1 and sys.argv[1] == "connect") :
        connect()
    elif len(sys.argv) > 1 and sys.argv[1] == "password" :
        identifiants()
    else : 
        print("USAGE: freewifi [ password ] [ connect ]")
    
