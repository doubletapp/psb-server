import json
import os
import urllib
import sys
import time
import pickle
import traceback
import numpy as np
sys.path.append('/home/serj/psb-server/')

from flask import Flask
from flask_mongoengine import MongoEngine

from keras.models import load_model
model = load_model("0_nails_cakes_unb_01_va0.9561.h5")

from PIL import Image
IMAGE_SIZE = 128


def img_as_np_array(file_name):
    img = Image.open(file_name, 'r')
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = np.array(img) / 255. - 0.5
    return img[:,:,:3]


def load_imgs(folder):
    imgs = []
    files = os.listdir(folder)
    for file in files:
        img = img_as_np_array(f"{folder}/{file}")
        imgs.append(img)
    imgs = np.array(imgs)
    return imgs

from settings import MONGODB_SETTINGS

from core.models import VkUserRequest
# from pymystem3 import Mystem
from pprint import pprint

app = Flask(__name__)
app.debug = True
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
db = MongoEngine(app)

# mystem = Mystem()


# def lemmatize_with_mystem(text):
#     words = [lemma for lemma in mystem.lemmatize(text) if not lemma.isspace() and not lemma.isnumeric()
#             and lemma.isalpha()]
#     return words
#
#
# def read_texts(file_names_in_classes, path_to_file = ""):
#     data = []
#     for class_index, per_classes in enumerate(file_names_in_classes):
#         for file_name in per_classes:
#             with open(f"{path_to_file}{file_name}") as file:
#                 text = file.read()
#                 asjson = json.loads(text)
#                 if 'response' not in asjson:
#                     continue
#                 items = asjson['response']['items']
#                 for i in items:
#                     post = i['text']
#                     if len(post.strip()) == 0:
#                         continue
#                     data.append(post)
#
#     return data


def analys_request(new_request):

    # with open('idf_vectorizer.pickle', 'rb') as f:
    #     idf_vectorizer = pickle.load(f)
    # with open('logistic_regression.pickle', 'rb') as f:
    #     log_regression = pickle.load(f)

    print("start analys_request")
    print("new_request")
    print(new_request)
    new_request.status = "in-progress"
    new_request.save()
    print(new_request)

    posts = json.loads(new_request.data["posts"])
    folder = f"users/imgs_{new_request.vk_user_id}"
    if not os.path.isdir(folder):
        os.mkdir(folder)
    try:
        # for item in posts:
        #     if "text" in item:
        #         X = idf_vectorizer.transform(item["text"]).toarray()
        #         predictions = log_regression.predict_proba(X)
        #         if predictions[0][1] > 0.5:
        #             new_request.result = {
        #                 "result": True,
        #                 "image_url": "https://sun9-22.userapi.com/c858416/v858416115/893d9/wyVJVTb8aRM.jpg",
        #                 "title": "Сдавай кватиру",
        #                 "subtitile": "Удобно и легально",
        #             }
        #             new_request.save()
        #             return True

        count = 0
        for item in posts:
            if 'attachments' in item:
                attachments = item['attachments']
                for attachment in attachments:
                    if attachment['type'] == 'photo':
                        for size in attachment['photo']['sizes']:
                            if size['type'] == 'q':
                                url = size['url']
                                urllib.request.urlretrieve(url, f"{folder}/{count}")
                                count += 1
                                time.sleep(0.1)
                                break

        imgs = load_imgs(folder)
        if len(imgs.shape) < 4:
            raise Exception("len(imgs.shape) < 4:")

        preds = model.predict(imgs)

        print("preds", preds)

        types = [0] * 3
        for i, p in enumerate(preds):
            types[np.argmax(p)] += 1

        print("types", types)

        result = np.array(types) / sum(types)

        print("result", result)

        if max(result[1], result[2]) > 0.01:
            if result[2] > result[1]:
                new_request.result = {
                    "result": True,
                    "image_url": "https://sun9-8.userapi.com/c858416/v858416115/893ed/_z06T5vFG_o.jpg",
                    "title": "Клиенты любят вашу выпечку",
                    "subtitile": "Радуйте их, а о налогах позаботимся мы",
                }
            else:
                new_request.result = {
                    "result": True,
                    "image_url": "https://sun9-8.userapi.com/c858416/v858416115/893e3/0h4NZkHn1aI.jpg",
                    "title": "Делай маникюр легально",
                    "subtitile": "Наши сервисы помогут организовать работу",
                }
        else:
            new_request.result["result"] = False

        new_request.status = "done"
        new_request.save()

    except Exception as ex:

        print(traceback.format_exc())

        new_request.result["result"] = False
        new_request.status = "done"
        new_request.save()

    return True




for new_request in VkUserRequest.objects(status="new"):
    analys_request(new_request)

