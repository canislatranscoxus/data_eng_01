#  ╔═════════════════════════════════════════════════════════╦═══╗
#  ║ This script prepare environment and deploy to GAE       ║ * ║
#  ╚═════════════════════════════════════════════════════════╩═══╝

#!/bin/bash

---------------------
# GCP Cloud.  Prepare python Virtual Environmet
#------------------------------------------------------------------------------

sudo apt-get install python3-venv
cd ~/git/
python3 -m venv ~/git/env
source ~/git/env/bin/activate

pip3 install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.54.2

# repository is already cloned
#git clone https://github.com/canislatranscoxus/data_eng_01.git
#git clone git@github.com:canislatranscoxus/data_eng_01.git

# update our files
cd ~/git/data_eng_01/
git pull
git pull --ff-only

# ------------------------------------------------------------------


# deploy Project
cd ~/git/data_eng_01/src/api/api

pip install -r requirements.txt


#  ╔═════════════════════════════════════════════════════════╦═══╗
#  ║ update *.yaml files                                     ║ * ║
#  ╚═════════════════════════════════════════════════════════╩═══╝


#------------------------------------------------------------------------------
# Deploy to GCP App Engine
#------------------------------------------------------------------------------
# Update Environment variables in app.yaml

cd ~/git/data_eng_01/src/api/api


gcloud app deploy --service-account=aatvelo4@appspot.gserviceaccount.com


gcloud app deploy
gcloud app browse

