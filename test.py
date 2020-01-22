from imageai.Prediction.Custom import CustomImagePrediction
import os
from os.path import join
from os import listdir

model = "./celebs-id/models/model_ex-045_acc-0.239583.h5"
class_json = "./celebs-id/json/model_class.json"

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(model)
prediction.setJsonPath(class_json)
prediction.loadModel(num_objects=10)

celeb_list = []
with open("list.txt", "r") as f:
    celeb_list = f.read().splitlines()

for celeb in celeb_list:
    print(celeb)
    celeb_test_dir_path = join("./celebs-id/test", celeb)

    for imgfile in listdir(celeb_test_dir_path):
        img_path = join(celeb_test_dir_path, imgfile)

        predictions, probabilities = prediction.predictImage(img_path, result_count=1)

        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction , " : " , eachProbability)

    print()
