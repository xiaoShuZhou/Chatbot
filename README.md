# Chatbot

## Chatbot website
http://20.115.5.160:8000/WebUI.html

## Requirement
1. Python 3.8
2. Rasa 2.8

## Clone the project
git clone https://github.com/xiaoShuZhou/Chatbot.git

## Configure ubuntu environment
sudo apt update  
sudo apt install python3-dev python3-pip

## create and activate virtual environment
python3 -m venv ./venv  
source ./venv/bin/activate

## Install RASA
pip3 install rasa

## Run project
nohup rasa run --enable-api --cors "*" &  
nohup rasa run actions &  
nohup python -m http.server &
