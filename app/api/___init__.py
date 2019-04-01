#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint


def create_blueprint(bpname):
    bp = Blueprint(bpname, __name__)
    return bp
