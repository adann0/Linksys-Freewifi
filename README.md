# Linksys-Freewifi
Etude de faisabilité - Améliorer un signal Hotspot Freewifi avec un routeur Linksys WRT54GL, le firmware DD-WRT et des antennes TP-Link 8dBi.

# Installation du Firmware DD-WRT

Dans un premier temps il faut télécharger le firmware pour notre routeur version MINI GENERIC sur le site de dd-wrt : https://dd-wrt.com/support/router-database/?model=WRT54GL_1.0/1.1

Ensuite il faut faire un Reset 30/30/30 sur le routeur (https://wiki.dd-wrt.com/wiki/index.php/Hard_reset_or_30/30/30).

Après le reset, si tout a fonctionné, l'interface web se trouve à l'adresse 192.168.1.1 (password : admin)

Dans Administration > Firmware Upgrade on met le firmware precedement téléchargé et on click sur Upgrade (ne pas quitter la page). A la fin on a un message "Upgrade Successful". On click sur continuer. (user : root / password : admin)

Pas besoin de refaire un reset 30/30/30 sauf si on veut upgrade sur un autre firmware dd-wrt (? à verifier).

# Configuration du Hotspot

# SpeedTest

# Sources

  Installer DD-WRT depuis le Firmware propriétaire : https://wiki.dd-wrt.com/wiki/index.php/Linksys_WRT54GL
  Hard Reset : https://wiki.dd-wrt.com/wiki/index.php/Hard_reset_or_30/30/30#Hard_Reset_.28aka_30.2F30.2F30_reset.29
  Configurer un Hotspot sur DD-WRT : http://www.lowcostmobile.com/actualite/1879-tutoriel-amplifier-signal-wifi-hotspot-communautaire-orange-freewifi-sfr-wifi-fon
