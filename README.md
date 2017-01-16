This is the code repo for the ecce-web-app. The application is based on python/django. Ecce-web-app is meant to publish/analyze data gahtered in the [ecce-project](http://ecce.univie.ac.at/).

# install

1. Clone the repo
2. Create a virtual environemt 
3. Run `pip install -r requirements.txt` to install needed packages
4. Change into the application's root directory and run `python manage.py runserver --settings=ecce.settings.dev`
5. The application should be accessible now under [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

# import legacy data

1. get lates data dumps from access-db
2. run `python manage.py shell_plus --notebook --settings=ecce.settings.{settingsFile}`
3. run `import_dates`
4. run `import_texts`
5. run `import_SchwaPresent`
6. run `import_onset`
7. run `import_TokenLabel`
8. run `import_Consonant`
9. rund `immport_Cluster`
10. and finally run `import_Tokens`. Since there are roughly 300.000 Tokens, the data files, stored in `data/access-export` are splitted. Therefore you have to change the name of the file in the `import_Tokens`.