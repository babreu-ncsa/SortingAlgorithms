###
# File: Sorter.py
# Description: Class to hold common sorter attributes and methods
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Thursday, 30th June 2022, 12:22:30 pm
# Last Modified: Tuesday, 5th July 2022, 2:49:51 pm
#  
# Copyright (c) 2022, Bruno R. de Abreu, National Center for Supercomputing Applications.
# All rights reserved.
# License: This program and the accompanying materials are made available to any individual
#          under the citation condition that follows: On the event that the software is
#          used to generate data that is used implicitly or explicitly for research
#          purposes, proper acknowledgment must be provided in the citations section of
#          publications. This includes both the author's name and the National Center
#          for Supercomputing Applications. If you are uncertain about how to do
#          so, please check this page: https://github.com/babreu-ncsa/cite-me.
#          This software cannot be used for commercial purposes in any way whatsoever.
#          Omitting this license when redistributing the code is strongly disencouraged.
#          The software is provided without warranty of any kind. In no event shall the
#          author or copyright holders be liable for any kind of claim in connection to
#          the software and its usage.
###

from auxiliaries.ScalingExperiment import ScalingExperimentResult
import numpy as np

class Sorter:
    def __init__(self):
        self.arraySize = 0
        self.input = np.zeros(0)
        self.output = np.zeros(0)

    def generateRandomArray(self, size):
        """
        Draws elements from the uniform distribution and populates array.

        Inputs:
            - size (int): number of elements in the array

        Updates:
            - self.input: array with the elements.
            - self.arraySize: the size of the array
        """
        import numpy as np
        self.arraySize = size
        self.input = np.random.rand(size)

        return

    def sortArray(self):
        """
        This function must be extended by subclasses of Sorter.
        """
        return


    def runScalingExperiment(self, scalingExpSpec):
        """
        Runs a scaling experiment for this sorter.
        """
        results = ScalingExperimentResult(scalingExpSpec)

        size = scalingExpSpec.initialSize
        for s in range(scalingExpSpec.nSizes):
            bestBlocks = np.zeros(scalingExpSpec.nBlocks)
            worstBlocks = np.zeros(scalingExpSpec.nBlocks)
            avgBlocks = np.zeros(scalingExpSpec.nBlocks)
            for b in range(scalingExpSpec.nBlocks):
                iters = np.zeros(scalingExpSpec.nStepsPerBlock)
                for it in range(scalingExpSpec.nStepsPerBlock):
                    self.generateRandomArray(size)
                    n = self.sortArray()
                    iters[it] = n
                bestBlocks[b] = iters.min()
                worstBlocks[b] = iters.max()
                avgBlocks[b] = iters.mean()
            results.bestAvg[s] = bestBlocks.mean()
            results.bestStd[s] = bestBlocks.std()
            results.worstAvg[s] = worstBlocks.mean()
            results.worstStd[s] = worstBlocks.std()
            results.avgAvg[s] = avgBlocks.mean()
            results.avgStd[s] = avgBlocks.std()

            size = size * scalingExpSpec.sizeMultiplier

        return results

    def checkSorting(self):
        """
        Checks to see if sorted array is sorted.
        """
        for i in range(self.arraySize-1):
            if self.output[i] > self.output[i+1]:
                return False
        return True