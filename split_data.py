#!/usr/bin/env python3

import os
import random
import shutil
import re
os.system('rm -rf ./training_data')
os.mkdir('./training_data')
os.mkdir('./training_data/train')
os.mkdir('./training_data/test')
os.mkdir('./training_data/val')
jpgs = [f for f in os.listdir('source_data') if f.endswith('.jpg')]
for jpg_filename in jpgs:
  r = random.random()
  txt_filename = re.sub('.jpg$', '.txt', jpg_filename)
  if r < .8:
    shutil.copyfile(f'source_data/{jpg_filename}', f'training_data/train/{jpg_filename}')
    shutil.copyfile(f'source_data/{txt_filename}', f'training_data/train/{txt_filename}')
  elif r < .9:
    shutil.copyfile(f'source_data/{jpg_filename}', f'training_data/test/{jpg_filename}')
    shutil.copyfile(f'source_data/{txt_filename}', f'training_data/test/{txt_filename}')
  else:
    shutil.copyfile(f'source_data/{jpg_filename}', f'training_data/val/{jpg_filename}')
    shutil.copyfile(f'source_data/{txt_filename}', f'training_data/val/{txt_filename}')
      