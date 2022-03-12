# -*- coding: utf-8 -*-
from flask import Blueprint

ad = Blueprint("ad", __name__, url_prefix="/admin")  # 给url添加 /admin，要使用 http://127.0.0.1:5000/admin/home 才能访问




@ad.route("/home")
def home():
    return "home界面"



