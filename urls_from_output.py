import requests
from os import mkdir
from os import path

def if_not_mkdir(name):
    if not path.exists(name):
        mkdir(name)

def get_urls():
    output = ''

    with open("output\colab_24jan_50epoch_240train.txt", "r") as f:
        output = f.read()

    d = {}

    c = 0
    celeb = None
    for line in output.splitlines():
        if line.strip() == "":
            continue

        if celeb is None:
            celeb = line.strip()
            d[celeb] = []

        else:
            if line.find("downloading") > -1:
                d[celeb].append(line.split()[1])
            elif line.find("done ") > -1:
                celeb = None
                c += 1
                if c == 10:
                    break
            else:
                pass

    '''for c in d.keys():
        print(c)
        print(len(d[c]))
        print(d[c][0:10])'''

    return d

def get_images(d):
    data_dir = ".\celebs-data\list300"
    if_not_mkdir(data_dir)

    for celeb in d.keys():
        print(celeb)
        celeb_data_dir = path.join(data_dir, celeb)
        if_not_mkdir(celeb_data_dir)

        c = 0
        ul = d[celeb]
        for img_url in ul[-61 : -1]:
            c += 1
            fn = str(c) + ".jpg"
            fp = path.join(celeb_data_dir, fn)
            if path.exists(fp):
                print("skipping", c)
                continue

            res = requests.get(img_url)
            img = res.content

            with open(fp, "wb") as f:
                f.write(img)

            print("downloaded", c)

d = get_urls()
get_images(d)