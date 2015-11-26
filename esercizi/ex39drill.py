# -*- coding: utf-8 -*-
#prova diz città italiane su esempio ex39


interr = "* " *30

capoluoghi = {
    "Piemonte": "TO",
    "Liguria": "GE",
    "Lombardia": "MI",
    "Veneto": "VE",
    "Toscana": "FI",
    "Umbria": "PG",
    "Campania": "NA",
    "Sicilia": "PA"
}

province = {
    "TO": "Torino",
    "GE": "Genova",
    "MI": "Milano",
    "VE": "Venezia",
    "FI": "Firenze",
    "PG": "Perugia",
    "NA": "Napoli",
    "PA": "Palermo"
}

#aggiungo capoluoghi
capoluoghi ["Marche"] = "AN"
capoluoghi ["Puglia"] = "BA"


#aggiungo province
province ["AN"] = "Ancona"
province ["BA"] = "Bari"

#visualizzo città e sigle
print interr
for sigla, citta in province.items():
    print "%s è %s" % (sigla, citta)

#visualizzo province e sigle
print interr
for regione, sigla in capoluoghi.items():
    print "%s è in %s." %(sigla, regione)

print "\ncioè:\n"

#unioneee
for regione, sigla in capoluoghi.items():
    print "%s è in %s." %(province[sigla], regione)

    assert 
