To bootstrap the creation of a configuration file for charts:
Start a django-shell session

> python manage.py shell_plus --settings=ecce.settings.postgres

and execute the following

```
from charts import chart_conf_creator
charts = chart_conf_creator.create()
```

This will create a file `charts\chart_config.py`. You can define the filename by adding a parameter to create() like, e.g.

> chart_conf_creator.create("whateverYouLike.py")

Now run `charts.store_config()` to create database entries form the config file created before.
