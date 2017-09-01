import json
import os
from browsing.filters import TokenListFilter


class ChartConfigurator():

    """A simple helper class to bootstrap rendering of charts"""

    def __init__(self, ListFilter, filename, default_charts=['bar', 'line', 'pie']):
        self.source = ListFilter()
        self.all_charts = default_charts
        self.filename = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

    def get_default_config(self):
        values = {}
        for x in self.source.declared_filters.items():
            values[x[0]] = {
                'label': x[1].label,
                'help_text': 'Provide some',
                'lookup_expr': x[1].lookup_expr,
                'chart_types': self.all_charts
            }
        return values

    def create_config_file(self):
        config_dict = self.get_default_config()
        config_json = json.dumps(
            config_dict, ensure_ascii=False, indent=4, sort_keys=True
        )
        with open(self.filename, 'w') as f:
            f.write(config_json)
        return config_dict


def create(filename="chart_config.py"):
    config_dict = ChartConfigurator(TokenListFilter, filename)
    return config_dict.create_config_file()
