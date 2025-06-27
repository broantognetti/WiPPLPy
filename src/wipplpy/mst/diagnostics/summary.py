import matplotlib.pyplot as plt
from wipplpy.modules.generic_get_data import Data as Data
import numpy as np
import xarray as xr
import MDSplus as mds

class PlasmaCurrent(Data):
    def __init__(self, tree):
            #Ordering does matter. Define calls, super init, then dimension specifications. Figuring out how to make it not matter, or streamline whats needed would be cool
            calls = ['\MST_OPS::IP_F'] #want to add ability to have multiple in this list
            super().__init__(tree, [True], calls) # could augment second argument as a keyword with Default None in which case it does all of calls
            self.units = ['kA', 's']
            self.names = ['plasma_current', 'shot_time']

    def plot(self):
        if not hasattr(self, "xarray"):
            self.get_xarray()
            print("Put together xarray")

        fig, ax = plt.subplots(figsize=(8,4))
        plt.plot(self.xarray.shot_time * 1000, self.xarray.data)
        ax.set_xlabel('Time (ms)')
        ax.set_ylabel('Plasma Current (kA)')
        plt.show()