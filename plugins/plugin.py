import os

import airflow
from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
from flask_appbuilder import expose, BaseView as AppBuilderBaseView
from airflow.security import permissions
from airflow.www.auth import has_access


# ANALYTICS HACK
class ClippyBlueprint(Blueprint):
    def __init__(self):
        super().__init__(
            "clippy",
            __name__,
            url_prefix="/clippy",
            static_url_path="/static/clippy",
            static_folder=os.path.join(os.path.dirname(__file__), "static"),
            template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        )

    def register(self, app, *args, **kwargs):
        app.jinja_loader.searchpath.append(self.template_folder)
        # gross terrible hack. We are hijacking the analytics pixel for our own nefarious purposes
        airflow.configuration.conf.set('webserver', 'analytics_tool', 'clippy')
        airflow.configuration.conf.set('webserver', 'analytics_id', '#####')


class Clippy(AppBuilderBaseView):
    default_view = "test"

    @expose("/")
    @has_access([(permissions.ACTION_CAN_READ, permissions.RESOURCE_WEBSITE), ])
    def test(self):
        return self.render_template("test.html", content="Hello galaxy!")


class ClippyPlugin(AirflowPlugin):
    name = "clippy"

    flask_blueprints = [ClippyBlueprint()]
    appbuilder_views = [{"view": Clippy()}]

# PHIL HACK
# class AstroClippyPlugin(AirflowPlugin):
#     name = "clippy"
#
#     flask_blueprints = [Blueprint(
#         "clippy",
#         __name__,
#         template_folder="templates",
#         static_folder="static",
#         static_url_path="/static/clippy"
#     )]
#
#     def on_load(*args, **kwargs):
#         import airflow.www.views as views
#         from types import FunctionType
#
#         f = views.AirflowBaseView.render_template
#
#         def handler(self, *args, **kwargs):
#             template = {
#                 "airflow/main.html": "test.html",
#             }.get(args[0], args[0])
#
#             return FunctionType(
#                 f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__
#             )(self, template, *args[1:], **kwargs)
#
#         views.AirflowBaseView.render_template = handler
