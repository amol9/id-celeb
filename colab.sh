#!/bin/bash

git clone https://github.com/amol9/id-celeb.git
cd id-celeb
python get.py
python split.py
pip install imageai
python train.py
