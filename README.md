# TaskMaster
Développer une application de gestion de projets qui s'intègre parfaitement avec Discord, permettant aux utilisateurs de gérer leurs tâches et projets sans quitter leur environnement de communication habituel.

##  API
Create a virtual env: `python3 venv <name of your venv>'
Activate the virtual env in linux: `source <name of your venv>/bin/activte`
Install the packages listed in the requirements.txt file: `pip install -r requirements.txt`
To launch the API navigate to the api/ directory and run `python3 app.py`
In your browser, open http://0.0.0.0:8080, and you will be automatically redirected to http://0.0.0.0:8080/api/ui/. After executing the GET request on /home, you should see the expected response message. 
![home](/api/home.png)

    gitGraph
       commit
       commit
       branch develop
       commit
       commit
       commit
       checkout main
       commit
       commit