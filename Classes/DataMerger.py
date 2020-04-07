import os

class DataMerger:
    def __init__(self, data_path):
        self.data_path= data_path


        if data_path+'Data.csv' not in os.listdir(data_path):
            self.output_file = open(data_path+'Data.csv', 'w+')

            first_file=True
            for file in os.listdir(data_path):
                if '.csv' in file:
                    with open(data_path+file, 'r') as f: text = f.readlines()
                    if first_file == True:
                        self.output_file.writelines(text)
                        first_file=False
                    else: self.output_file.writelines(text[1:])
            self.output_file.close()
        else:
            print('Data.csv already present')

        self.merged_data = data_path+'Data.csv'
