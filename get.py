import requests
import sys
from os.path import join, exists
from os import mkdir


def get_celeb(name):
    limit = 70
    data_dir = "./celebs-data"


    url_base = "https://reddit.com/r/"

    subreddit = name
    data_sub_dir = join(data_dir, subreddit)

    if not exists(data_sub_dir):
        mkdir(data_sub_dir)

    url = url_base + subreddit + "/new.json?limit=200"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})


    res_json = res.json()
    print("result count:", len(res_json['data']['children']))

    c = 0
    for i in res_json['data']['children']:
        image_url = i['data']['url']
        #print(image_url)
        if (image_url.endswith('jpg')):
            c += 1
            if not exists(join(data_sub_dir, (str(c+1) + '.jpg'))):
                print(image_url)
                img_res = requests.get(image_url)
                img_path = join(data_sub_dir, str(c) + '.jpg')
                with open(img_path, 'wb') as f:
                    f.write(img_res.content)

        if c == limit:
            print("done", limit)


def get_all():
    celeb_list = []
    with open("list.txt", "r") as f:
        celeb_list = f.read().splitlines()

    for celeb in celeb_list:
        print(celeb)
        get_celeb(celeb)

if len(sys.argv) > 1:
    get_celeb(sys.argv[1])
else:
    get_all()