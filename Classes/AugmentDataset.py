import pandas as pd
import matplotlib.pyplot as plt



class AugmentDataset:

    def __init__(self, data):

        data['Date'] = data.Year.astype(str) + '-' + data.Month.astype(str) + '-' + data.Day.astype(str)
        data['Time'] = data.Hour.astype(str) + ':' + data.Minute.astype(str)
        data['Dow'] = pd.DatetimeIndex(
            data.Year.astype(str) + '-' + data.Month.astype(str) + '-' + data.Day.astype(str)).dayofweek

        self.data = data


class CharctherizeDataset:

    def __init__(self, data):
        rename_dict = {'Year': 'Events'}
        self.events_per_day = data.groupby(data['Date']).count().rename(columns=rename_dict)['Events']
        self.events_per_hour = data.groupby(data['Hour']).count().rename(columns=rename_dict)['Events']
        self.events_per_dow = data.groupby(data['Dow']).count().rename(columns=rename_dict)['Events']

        self.metrics = dict(day=self.events_per_day, hour=self.events_per_hour, dow= self.events_per_dow)

    def plot(self, metrics, save=False, plot_dir_path='../Plots/'):

        fig, ax = plt.subplots(len(metrics), 1)
        for index, metric in enumerate(metrics):
            self.metrics[metric].plot.bar(ax=ax[index])
            if metric=='day':
                ax[index].set_xticklabels([])



        if save == True:
            plt.savefig(plot_dir_path+'Characterization.pdf', bbox_inches='tight')

        plt.show()
