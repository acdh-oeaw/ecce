This is the code repo for the ecce-web-app. The application is based on python/django.

# import legacy data

1. get lates data dumps from access-db
2. run `python manage.py shell_plus --notebook --settings=ecce.settings.{settingsFile}`
3. run `import_dates`
4. run `import_texts`