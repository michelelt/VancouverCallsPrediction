import sys
sys.path.append('..')
from Classes.DataMerger import DataMerger
from Classes.AugmentDataset import AugmentDataset
from Classes.AugmentDataset import CharctherizeDataset


import pandas as pd

data_path = '../Data/'

dm = DataMerger(data_path)
data = pd.read_csv(dm.merged_data)

aug_data = AugmentDataset(data)
data = aug_data.data

char_data = CharctherizeDataset(data)
char_data.plot(['day', 'hour', 'dow'], save=True)








