import os

import airflow
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint


class ClippyBlueprint(Blueprint):
    def __init__(self):
        super().__init__(
            "astro_clippy",
            __name__,
            # url_prefix="/clippy",
            static_url_path="/static/clippy",
            static_folder=os.path.join(os.path.dirname(__file__), "static"),
            template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        )

    def register(self, app, *args, **kwargs):
        app.jinja_loader.searchpath.append(self.template_folder)
        # gross terrible hack. We are hijacking the analytics pixel for our own nefarious purposes
        airflow.configuration.conf.set('webserver', 'analytics_tool', 'astro_clippy')
        airflow.configuration.conf.set('webserver', 'analytics_id', '#####')


class AstroClippyPlugin(AirflowPlugin):
    name = "astro_clippy"
    flask_blueprints = [ClippyBlueprint()]
