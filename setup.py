# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_plugin_export']

package_data = \
{'': ['*']}

install_requires = \
['poetry-core>=1.6.0,<2.0.0', 'poetry>=1.5.0,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['export = '
                               'poetry_plugin_export.plugins:ExportApplicationPlugin']}

setup_kwargs = {
    'name': 'poetry-plugin-export',
    'version': '1.5.0',
    'description': 'Poetry plugin to export the dependencies to various formats',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://python-poetry.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
