from imageai.Prediction.Custom import CustomImagePrediction
import os
from os.path import join
from os import listdir
import json
import sys

config = None
with open(sys.argv[1], "r") as f:
    config = json.load(f)

data_dir = config['data_dir']
model_fn = config['model']
model = join(data_dir, "models", model_fn)
class_json = join(data_dir, "json", "model_class.json")

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(model)
prediction.setJsonPath(class_json)
prediction.loadModel(num_objects=10)

celeb_list = []
list_fn = config['list']
with open(list_fn, "r") as f:
    celeb_list = f.read().splitlines()

right = 0
wrong = 0
total = 0

for celeb in celeb_list:
    print(celeb)
    c_right = 0
    c_wrong = 0
    c_total = 0

    celeb_test_dir_path = join(data_dir, "test", celeb)

    for imgfile in listdir(celeb_test_dir_path):
        img_path = join(celeb_test_dir_path, imgfile)
        c_total += 1

        predictions, probabilities = prediction.predictImage(img_path, result_count=1)

        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , eachProbability)
            if eachPrediction == celeb:
                c_right += 1
            else:
                c_wrong += 1

    right += c_right
    wrong += c_wrong
    total += c_total

    print("acc: %f"%(c_right/c_total))

    print()

print("overall acc: %f"%(right/total))