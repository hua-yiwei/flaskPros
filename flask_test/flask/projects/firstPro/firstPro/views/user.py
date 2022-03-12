# -*- coding: utf-8 -*-
from flask import Blueprint

us = Blueprint("us", __name__)


# 在这里加 before_request ，请求的url是user.py模块的才会执行bf函数
@us.before_request
def bf():
    print("请求前")


@us.route("/user")
def user():
    return "user页面"
