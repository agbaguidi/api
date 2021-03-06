# -*- coding: utf-8 -*-
"""
:author: ludovic.delaune@oslandia.com

This module contains the WSGI application used by Flask development server
and any production WSGI deployments
"""
from prkng import create_app
from prkng.api.admin import init_admin
from prkng.api.explorer import init_explorer
from prkng.api.public import init_api, v0, v1
from prkng.api.partners.car2go import init_car2go
from prkng.api.partners.communauto import init_communauto
from prkng.logger import Logger
from prkng.login import init_login
from prkng.models import init_model

app = create_app()
init_model(app)
init_api(app)
init_login(app)
init_admin(app)
init_car2go(app)
init_communauto(app)
init_explorer(app)

Logger.debug(app.config)
