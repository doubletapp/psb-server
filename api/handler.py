import json
import random

from flask import Blueprint


def check_self_employed():
    result1 = {
        "result": True,
        "image_url": "https://sun9-18.userapi.com/c858016/v858016735/8cd15/uAZxmks0RRM.jpg",
        "title": "Клиенты любят вашу выпечку",
        "subtitile": "Радуйте их, а о налогах позаботимся мы",
    }

    result2 = {
        "result": False,
    }

    return json.dumps(random.choice([result1, result2]))


api_blueprint = Blueprint('root', __name__)
api_blueprint.add_url_rule('/check_self_employed', view_func=check_self_employed, methods=['post'])


def fav():
    return ""


api_blueprint.add_url_rule('/favicon.ico', view_func=fav)
