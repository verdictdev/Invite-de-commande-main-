@echo off
REM Vérifier si pip est installé
python -m ensurepip --default-pip

REM Mettre à jour pip
python -m pip install --upgrade pip

REM Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

REM Exécuter le script Python idc.py
python idc.py

pause
