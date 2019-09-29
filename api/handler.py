import json
from core.models import VkUserRequest
from api.self_employed_analyses import analys_request

from flask import Blueprint, request
import threading





def check_self_employed():

    data = request.json.get('data')
    vk_user_id = request.json.get('vk_user_id')

    new_request = VkUserRequest.objects.create(data=data, vk_user_id=vk_user_id)

    result = {
        "request_id": str(new_request.id)
    }
    print("Thread start")
    threading.Thread(target=analys_request, args=(str(new_request.id),)).start()
    print("Thread next")

    return json.dumps(result)


def check_request():
    request_id = request.json.get('request_id')

    try:
        old_request = VkUserRequest.objects.get(id=request_id)
    except Exception as ex:
        return json.dumps({"result": False, "error": True})

    return json.dumps(old_request.result)

    # result1 = {
    #     "result": True,
    #     "image_url": "https://sun9-18.userapi.com/c858016/v858016735/8cd15/uAZxmks0RRM.jpg",
    #     "title": "Клиенты любят вашу выпечку",
    #     "subtitile": "Радуйте их, а о налогах позаботимся мы",
    # }
    #
    # result2 = {
    #     "result": False,
    # }

    # return json.dumps(random.choice([result1, result2]))


api_blueprint = Blueprint('root', __name__)
api_blueprint.add_url_rule('/check_self_employed', view_func=check_self_employed, methods=['post'])
api_blueprint.add_url_rule('/check_request', view_func=check_request, methods=['post'])


def fav():
    return ""


api_blueprint.add_url_rule('/favicon.ico', view_func=fav)
