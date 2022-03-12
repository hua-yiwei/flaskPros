# -*- coding: utf-8 -*-
from flask import Blueprint

ac = Blueprint("ac", __name__)


@ac.route("/login")
def login():
    return "登录页面"


@ac.route("/logout")
def logout():
    return "退出登录"
