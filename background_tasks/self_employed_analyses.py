import json
import os
import urllib
import sys
import time
sys.path.append('/home/serj/psb-server/')

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
    posts = json.loads(new_request.data.get(["posts"]))

    count = 0
    for item in posts:
        if 'attachments' in item:
            attachments = item['attachments']
            for attachment in attachments:
                if attachment['type'] == 'photo':
                    for size in attachment['photo']['sizes']:
                        if size['type'] == 'q':
                            url = size['url']
                            folder = f"users/imgs_{new_request.vk_user_id}"
                            if not os.path.isdir(folder):
                                os.mkdir(folder)
                            urllib.request.urlretrieve(url, f"{folder}/{count}")
                            count += 1
                            time.sleep(0.1)
                            break