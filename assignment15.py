#!/usr/bin/env python
from assignment8 import StressStrainConverter
import numpy as np
import scipy.integrate

class ParallelToughness(StressStrainConverter):

    def __init__(self, filename, comm):
        super().__init__(filename)

        self.comm = comm
        self.rank = comm.rank
        self.size = comm.size

        if self.rank == 0:
            self.convert_to_true_stress_and_strain()
        else:
            self.true_stress = []
            self.true_strain = []


    def compute_toughness(self):

        #####################
        ### Add code here ###
        #####################

        return 
