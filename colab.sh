#!/bin/bash

cd id-celeb
python get.py
python split.py
pip install imageai
python train.py
