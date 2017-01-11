# charts
A django application to visualize data using [Highcharts](http://www.highcharts.com/).
##install
1. Copy the `charts` directory into your django project
2. Register `charts` in your settings file under `INSTALLED_APPS = [..., 'charts', ...]`
3. Include the application's URLS to the project's main `urls.py`: `urlpatterns = [...,
    url(r'charts/', include('charts.urls', namespace='charts')), ...]`
4. Browse to [{root}/charts/barcharts/](http://127.0.0.1:8000/charts/barcharts/)
5. If everything works, you should see a simple [bar](https://dig-ed-cat.eos.arz.oeaw.ac.at/charts/barcharts/) and [pie](https://dig-ed-cat.eos.arz.oeaw.ac.at/charts/piecharts/) chart.




