from os.path import join, exists
from os import mkdir
from shutil import copyfile
import json
import sys

config = None
with open(sys.argv[1], "r") as f:
    config = json.load(f)


celeb_list = []
with open("list300.txt", "r") as f:
    celeb_list = f.read().splitlines()

data_dir = config['dst_dir']
if not exists(data_dir):
    mkdir(data_dir)

#size = 300
test = config['test']
train = config['train']

test_dir = join(data_dir, "test")
train_dir = join(data_dir, "train")

if not exists(test_dir):
    mkdir(test_dir)

if not exists(train_dir):
    mkdir(train_dir)

src_data_dir = config['src_dir']

for celeb in celeb_list:
    celeb_test_dir = join(test_dir, celeb)
    if not exists(celeb_test_dir):
        mkdir(celeb_test_dir)

    celeb_train_dir = join(train_dir, celeb)
    if not exists(celeb_train_dir):
        mkdir(celeb_train_dir)

    celeb_src_dir = join(src_data_dir, celeb)

    for i in range(1, train+1):
        filename = str(i) + '.jpg'
        src_filename = join(celeb_src_dir, filename)
        dst_filename = join(celeb_train_dir, filename)
        copyfile(src_filename, dst_filename)

    for i in range(1+train, train+test+1):
        filename = str(i) + '.jpg'
        src_filename = join(celeb_src_dir, filename)
        dst_filename = join(celeb_test_dir, filename)
        copyfile(src_filename, dst_filename)

    