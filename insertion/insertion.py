###
# File: insertion.py
# Description: Insertion sort 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 28th June 2022, 3:01:29 pm
# Last Modified: Wednesday, 29th June 2022, 8:10:11 am
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
from ScalingExperiment import ScalingExperimentSpec, ScalingExperimentResult
import numpy as np

class InsertionSorter:

    def __init__(self):
        import numpy as np
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
        Sorts array using Insertion Sort
        https://en.wikipedia.org/wiki/Insertion_sort

        Returns:
            - nSteps (int): total number of iterations to sort the array

        Updates:
            - self.output: the sorted array
        """
        if (self.arraySize == 0):
            print("Please generate array!")
            return 0
        
        nSteps = 0
        self.output = self.input
        for i in range(1, len(self.output), 1):
            x = self.output[i]
            j = i - 1
            while j >= 0 and self.output[j] > x:
                self.output[j+1] = self.output[j]
                j = j - 1
                nSteps = nSteps + 1
            self.output[j+1] = x

        return nSteps


    def runScalingExperiment(self, scalingExpSpec):
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
