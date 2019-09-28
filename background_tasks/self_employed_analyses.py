import json

from flask import Flask
from flask_mongoengine import MongoEngine

from settings import MONGODB_SETTINGS

from core.models import VkUserRequest
from pprint import pprint

app = Flask(__name__)
app.debug = True
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
db = MongoEngine(app)

for new_request in VkUserRequest.objects(status="new"):
    new_request.status = "in-progress"
    # new_request.save()
    posts = json.loads(new_request.data["posts"])