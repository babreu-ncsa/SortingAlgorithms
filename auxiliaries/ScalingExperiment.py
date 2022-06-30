###
# File: ScalingExperimentSpec.py
# Description: A class to host Specifications of a Scaling Experiment
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 29th June 2022, 7:24:24 am
# Last Modified: Wednesday, 29th June 2022, 7:49:41 am
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

class ScalingExperimentSpec:
    def __init__(self, initialSize, sizeMultiplier, nSizes, nBlocks, nStepsPerBlock):
        """
        Initializes an instance of this class.

        Inputs:
            - initialSize (int): the array size to start the experiment with.
            - sizeMultiplier (int): the multiplication factor for the size on each loop.
            - nSizes (int): the total number of array sizes to consider.
            - nBlocks (int): the number of blocks, for each size, to get statistics from.
            - nStepsPerBlock (int): the number of sorts in each block.
        """
        self.initialSize = initialSize
        self.sizeMultiplier = sizeMultiplier
        self.nSizes = nSizes
        self.nBlocks = nBlocks
        self.nStepsPerBlock = nStepsPerBlock

class ScalingExperimentResult:
    def __init__(self, scalingExpSpec):
        """
        Initializes an instance of this class, which stores results for the best, worst, and average number of iterations over the blocks for each array size.


        Inputs:
            - scalingExpSpec (ScalingExperimentSpec): the specs for this experiment
        """
        import numpy as np
        self.bestAvg = np.zeros(scalingExpSpec.nSizes) 
        self.bestStd = np.zeros(scalingExpSpec.nSizes) 
        self.worstAvg = np.zeros(scalingExpSpec.nSizes) 
        self.worstStd = np.zeros(scalingExpSpec.nSizes) 
        self.avgAvg = np.zeros(scalingExpSpec.nSizes) 
        self.avgStd = np.zeros(scalingExpSpec.nSizes)
        finalSize = scalingExpSpec.initialSize * (scalingExpSpec.sizeMultiplier ** (scalingExpSpec.nSizes - 1)) 
        self.arraySizes = np.geomspace(scalingExpSpec.initialSize, finalSize, scalingExpSpec.nSizes)
