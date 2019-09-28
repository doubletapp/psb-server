from mongoengine import DictField, Document, StringField, IntField


class VkUserRequest(Document):
    status = StringField(required=True, choices=["done", "new", "in-progress"], default="new")
    vk_user_id = IntField(required=True)
    data = DictField(required=True)
    result = DictField(default={"result": False})



