# Linksys-Freewifi
Etude de faisabilité - Améliorer un signal Hotspot Freewifi/Public avec un routeur Linksys WRT54GL, le firmware DD-WRT et des antennes TP-Link 8dBi.

# Installation du Routeur

Le mieux est de tester le tout dans un premier temps sur sa propre connection si on vient de recevoir le routeur :

    - Deconnecter tout les appareils du réseau
    - Débrancher la Freebox (modem)
    - Connecter le routeur à la Freebox par le port Internet
    - Connecter le routeur à un Raspberry ou un ordinateur disposant d'un port Ethernet pouvant être relié au routeur...
    - Mettre en route la Freebox (modem)
    - Mettre en route le Routeur
    - Mettre en route le Raspberry (ordinateur)
    
Une fois sur le Raspberry (testé en HDMI, pas SSH) le routeur est à l'adresse 192.168.1.1 et le mot de passe est "admin". Si on est connecté a l'interface web le routeur fonctionne - on peut changer le "routeur name" par exemple, pour être sur que le Hard Reset que l'on va faire ensuite se sera bien passé - et on passe a l'étape suivante.

# Installation du Firmware DD-WRT

https://wiki.dd-wrt.com/wiki/index.php/Linksys_WRT54GL

Dans un premier temps il faut télécharger le firmware pour notre routeur version MINI GENERIC sur le site de dd-wrt : https://dd-wrt.com/support/router-database/?model=WRT54GL_1.0/1.1

Ensuite il faut faire un Reset 30/30/30 sur le routeur (https://wiki.dd-wrt.com/wiki/index.php/Hard_reset_or_30/30/30).

Après le reset, si tout a fonctionné, l'interface web se trouve à l'adresse 192.168.1.1 (password : admin) - et le routeur s'appel de nouveau WRT54GL.

Dans Administration > Firmware Upgrade on met le firmware precedement téléchargé et on click sur Upgrade (ne pas quitter la page). A la fin on a un message "Upgrade Successful". On click sur continuer et si on retourne sur 192.168.1.1 on a la page de DD-WRT.

Ensuite il faut refaire un Reset 30/30/30. On retourn sur 192.168.1.1, on définit le nom d'utilisateur et le mot de passe et l'installation est completée.

# Configuration du Hotspot

# SpeedTest

# Sources

  Installer DD-WRT depuis le Firmware propriétaire : https://wiki.dd-wrt.com/wiki/index.php/Linksys_WRT54GL
  Hard Reset : https://wiki.dd-wrt.com/wiki/index.php/Hard_reset_or_30/30/30#Hard_Reset_.28aka_30.2F30.2F30_reset.29
  Configurer un Hotspot sur DD-WRT : http://www.lowcostmobile.com/actualite/1879-tutoriel-amplifier-signal-wifi-hotspot-communautaire-orange-freewifi-sfr-wifi-fon
