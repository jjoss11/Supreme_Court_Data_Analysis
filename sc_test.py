from buildVoc import build_voc
from bag_of_words import feat_vec
import os
import numpy as np


mylist = [x for x in os.listdir('dir') if x.endswith('.pdf')]
voc = []
voc = build_voc(mylist, voc)

features = [0]*len(voc)

for f in mylist:
    new_row = feat_vec('dir/' + f, voc)
    features = np.vstack([features, new_row])

features = np.delete(features, 0, 0)
print(features)
