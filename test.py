import requests



for i in range(1):
    result = requests.post("http://psb.doubletapp.ru/check_self_employed",
                           json={

                               "data": {
                                   "goods": "[{\"availability\":0,\"category\":{\"id\":306,\"name\":\"Movies, Music, Software\",\"section\":{\"id\":3,\"name\":\"Computers\"}},\"date\":1569344226,\"description\":\"Описание товара\",\"id\":3469710,\"owner_id\":560429707,\"price\":{\"amount\":\"1000\",\"currency\":{\"id\":643,\"name\":\"RUB\"},\"text\":\"10 rub.\"},\"thumb_photo\":\"https:\\/\\/sun9-48.userapi.com\\/c850424\\/v850424253\\/1c55a1\\/PZUIM6csXaU.jpg\",\"title\":\"Название товара\",\"albums_ids\":[],\"photos\":[{\"id\":457239017,\"album_id\":-53,\"owner_id\":560429707,\"sizes\":[{\"type\":\"m\",\"url\":\"https:\\/\\/sun9-25.userapi.com\\/c850424\\/v850424253\\/1c558d\\/tZG2oj-o3rI.jpg\",\"width\":130,\"height\":102},{\"type\":\"o\",\"url\":\"https:\\/\\/sun9-20.userapi.com\\/c850424\\/v850424253\\/1c5592\\/K7n4odC9JJA.jpg\",\"width\":130,\"height\":102},{\"type\":\"p\",\"url\":\"https:\\/\\/sun9-17.userapi.com\\/c850424\\/v850424253\\/1c5593\\/oJNo6rL71Ms.jpg\",\"width\":200,\"height\":158},{\"type\":\"q\",\"url\":\"https:\\/\\/sun9-38.userapi.com\\/c850424\\/v850424253\\/1c5594\\/PWK-o_yj0x4.jpg\",\"width\":320,\"height\":252},{\"type\":\"r\",\"url\":\"https:\\/\\/sun9-56.userapi.com\\/c850424\\/v850424253\\/1c5595\\/JXoqDaecShg.jpg\",\"width\":510,\"height\":402},{\"type\":\"s\",\"url\":\"https:\\/\\/sun9-28.userapi.com\\/c850424\\/v850424253\\/1c558c\\/OTskQVhyKFs.jpg\",\"width\":75,\"height\":59},{\"type\":\"w\",\"url\":\"https:\\/\\/sun9-4.userapi.com\\/c850424\\/v850424253\\/1c5591\\/23jC3usjtpQ.jpg\",\"width\":1980,\"height\":1560},{\"type\":\"x\",\"url\":\"https:\\/\\/sun9-5.userapi.com\\/c850424\\/v850424253\\/1c558e\\/EASRJLNAJZw.jpg\",\"width\":604,\"height\":476},{\"type\":\"y\",\"url\":\"https:\\/\\/sun9-13.userapi.com\\/c850424\\/v850424253\\/1c558f\\/eADMFN-ULp0.jpg\",\"width\":807,\"height\":636},{\"type\":\"z\",\"url\":\"https:\\/\\/sun9-45.userapi.com\\/c850424\\/v850424253\\/1c5590\\/C2HkabKtqjA.jpg\",\"width\":1280,\"height\":1008}],\"text\":\"\",\"date\":1569344214}],\"can_comment\":1,\"can_repost\":1,\"likes\":{\"count\":0,\"user_likes\":0},\"reposts\":{\"count\":0},\"views_count\":2}]",
                                   "groups": "[{\"id\":186027898,\"name\":\"VK Hackathon'19 | ON BOARD\",\"screen_name\":\"hack_onboard19\",\"is_closed\":1,\"type\":\"group\",\"is_admin\":0,\"is_member\":1,\"is_advertiser\":0,\"photo_50\":\"https:\\/\\/sun9-50.userapi.com\\/c858128\\/v858128863\\/6d6af\\/LSbKZzAgIYc.jpg?ava=1\",\"photo_100\":\"https:\\/\\/sun9-37.userapi.com\\/c858128\\/v858128863\\/6d6ae\\/XAF4sIo6F_U.jpg?ava=1\",\"photo_200\":\"https:\\/\\/sun9-31.userapi.com\\/c858128\\/v858128863\\/6d6ad\\/DHSKzVteofI.jpg?ava=1\"},{\"id\":103600381,\"name\":\"VK Hackathon\",\"screen_name\":\"hackathon\",\"is_closed\":0,\"type\":\"group\",\"is_admin\":0,\"is_member\":1,\"is_advertiser\":0,\"photo_50\":\"https:\\/\\/sun9-1.userapi.com\\/c858332\\/v858332105\\/25b78\\/CJiFfsKzL9k.jpg?ava=1\",\"photo_100\":\"https:\\/\\/sun9-66.userapi.com\\/c858332\\/v858332105\\/25b77\\/3QXOp9eDtLw.jpg?ava=1\",\"photo_200\":\"https:\\/\\/sun9-43.userapi.com\\/c858332\\/v858332105\\/25b76\\/prs1u2SamHM.jpg?ava=1\"},{\"id\":99988726,\"name\":\"Doubletapp | Студия разработки\",\"screen_name\":\"doubletapp\",\"is_closed\":0,\"type\":\"page\",\"is_admin\":0,\"is_member\":1,\"is_advertiser\":0,\"photo_50\":\"https:\\/\\/sun9-14.userapi.com\\/c854024\\/v854024338\\/80c27\\/rlbSRKUp6ic.jpg?ava=1\",\"photo_100\":\"https:\\/\\/sun9-99.userapi.com\\/c854024\\/v854024338\\/80c26\\/dQYdkQPtIJg.jpg?ava=1\",\"photo_200\":\"https:\\/\\/sun9-5.userapi.com\\/c854024\\/v854024338\\/80c25\\/ixgvvEa5Y14.jpg?ava=1\"}]",
                                   "notes": "[]", "posts": "[]"
                               },
                               "vk_user_id": "560429707",



                           })
    print(result.text)