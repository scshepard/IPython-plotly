import os

from django.conf import settings


def items():
    items = [
        dict(
            location='/ipython-notebooks/network-graphs',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'networkx',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/subplots',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'make_subplots',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/basemap-maps',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'basemap',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/collaboration',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'collaborate',
                'body.html'),
            priority=0.5
        )
    ]
    return items
