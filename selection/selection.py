###
# File: selection.py
# Description: Selection sort
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Thursday, 30th June 2022, 12:20:13 pm
# Last Modified: Thursday, 30th June 2022, 12:48:15 pm
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

from auxiliaries.Sorter import Sorter

class SelectionSorter(Sorter):

    def sortArray(self):
        """
        Sorts array using Selection Sort
        https://en.wikipedia.org/wiki/Selection_sort

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
        for i in range(0, len(self.output)-1, 1):
            jMin = i
            # go over array and find the minimum
            for j in range(i+1, len(self.output), 1):
                if(self.input[j] < self.input[jMin]):
                    jMin = j
                nSteps = nSteps + 1
            if (jMin != i):
                self.output[i] = self.input[jMin]

        return nSteps



