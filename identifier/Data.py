from torch.utils.data import Dataset, DataLoader
from identifier.Utils import *

class Data(Dataset):
    def __init__(self, path):
        self.x, self.y = self.generate_datasets(path)
        self.len = self.y.shape[0]


    def generate_datasets(self, path):
        for fname in diriter(path):
            json = jsonload(fname)
            zas = json['document'][0]['ZA']
            sentences = json['document'][0]['sentence']

            for za in zas:
                predicate = za['predicate']
                antecedent = za['antecedent'][0]

                if predicate['sentence_id'] == predicate['sentence_id']:
                    continue  # remove intra-sentential ZA

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.len
