# Instalation

1. Instalation d'elasticsearch 

Suivre les instruction mise à jour a l'adresse : https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html


2. ```git clone https://gitlab.com/MohamedBouchiba/siacl_engin.git```

3. ```cd siacl_engin```

4. Si vous n'avez pas vitrualenv d'instaler sur votre machine : ```pip install virtualenv``` 

   Sinon :  ```virtualenv venv``` 

5. Activation de l'environement.
* Ubuntu / MacOs : ```source venv/bin/activate```
* Windows : ```source venv/Scripts/activate```

6. ```pip install elasticsearch-loader```

7. Instalation des dépandance du projet : ```pip install -r requirements.txt```

8. Lancer elasticsearch :

* Ubuntu / MacOs : ```service elasticsearch start```
* Windows : ce rendre dans le dossier elasticsearch et executer ```.\bin\elasticsearch```

9. Création d'un de l'index "*avis_siacl*". Pensez à bien verifier le port utiliser par elasticsearch
```curl -XPUT localhost:9200/avis_siacl```

10. Chargement des avis du siacl sur l'index elasticsearch crée en amont. 
```elasticsearch_loader --index avis_siacl --type incident json nom_du_fichier_json_des_avis.json```

Variables  | Descriptions
------------- | -------------
nom_du_fichier_json_des_avis.json | mettre le chemin d'accer du fichers des avis générer par l'extracteur [SIACL_to_PDF](https://gitlab.com/MohamedBouchiba/siacl_to_pdf "Extracteur d'inforamtion d'avis au format pdf to json")
avis_siacl | l'index dans le quel nous allon charger les donner.


11. Configuration de flask
```export FLASK_APP=app.py```

12. Lancer le serveur web
```flask run```

13. Se rendre sur : http://127.0.0.1:5000/

14. Copier coller le dossier avec le quel vous avez générer le fichier JSON

<details><summary>Fini ?</summary>
<p>

## Bravo !

<details><summary>:D</summary>
<p>

#### j'espère que cela a été clair !


</p>
</details>

</p>
</details>