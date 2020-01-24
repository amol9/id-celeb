import requests
import sys
from os.path import join, exists
from os import mkdir, listdir

dbg = True
limit = 300

def dbg_print(s):
    if dbg:
        print(s)

def get_celeb(name):
    data_dir = "./celebs-data"

    if not exists(data_dir):
        mkdir(data_dir)


    url_base = "https://reddit.com/r/"

    subreddit = name
    data_sub_dir = join(data_dir, subreddit)

    if not exists(data_sub_dir):
        mkdir(data_sub_dir)
    else:
        count = len(listdir(data_sub_dir))
        if count >= limit:
            return count

    c = 0
    after = None
    while c < limit:
        url = url_base + subreddit + "/new.json?limit=100" + ("&after=" + after if after else "")
        dbg_print(url)
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res_json = res.json()
        dbg_print("result count: " + str(len(res_json['data']['children'])))
        after = res_json['data']['after']
        dbg_print("after: " + str(after))

        for i in res_json['data']['children']:
            image_url = i['data']['url']
            dbg_print(image_url)
            if (image_url.endswith('jpg')):
                c += 1
                if not exists(join(data_sub_dir, (str(c+1) + '.jpg'))):
                    dbg_print("downloading " + image_url)
                    img_res = requests.get(image_url)
                    img_path = join(data_sub_dir, str(c) + '.jpg')
                    with open(img_path, 'wb') as f:
                        f.write(img_res.content)

            if c == limit:
                print("done", limit)
                return limit

        if after is None or after == "":
            print("done", c)
            return c




def get_all():
    celeb_list = []
    with open("list300.txt", "r") as f:
        celeb_list = f.read().splitlines()

    for celeb in celeb_list:
        print(celeb)
        c = get_celeb(celeb)
        summary.append((celeb, c))

summary = []

if len(sys.argv) > 1:
    c = get_celeb(sys.argv[1])
    summary.append((sys.argv[1], c))
else:
    get_all()

for n, c in summary:
    print(n, ":", c)