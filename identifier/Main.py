import os
import torch
from identifier.Data import *

class Main:
    def __init__(self, mode, model_name):
        self.model_name = model_name

    def save_model(self):
        torch.save(self.model.state_dict(), "models/%s" % self.model_name)
        self.args.save()

    def load_model(self):
        self.model.load_state_dict(torch.load("models/%s" % self.model_name, map_location=self.device))

    def train(self, train_path, test_path):
        train_data = Data(train_path)
        return


if __name__ == "__main__":
    print(os.path.abspath(__file__))

    write_path = r'/data/za_korean/data/write_0226'
    speak_path = r'/data/za_korean/data/speak_0226'

    main = Main('train', '0312_1')
    main.train(write_path, '')