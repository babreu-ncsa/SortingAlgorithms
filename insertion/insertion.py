###
# File: insertion.py
# Description: Insertion sort 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 28th June 2022, 3:01:29 pm
# Last Modified: Thursday, 7th July 2022, 2:41:53 pm
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

class InsertionSorter(Sorter):
    
    def sortArray(self):
        """
        Sorts array using Insertion Sort
        https://en.wikipedia.org/wiki/Insertion_sort

        Returns:
            - time (float): elapsed time to sort the array

        Updates:
            - self.output: the sorted array
        """
        import time

        if (self.arraySize == 0):
            print("Please generate array!")
            return 0
        
        start = time.perf_counter()
        self.output = self.input
        for i in range(1, len(self.output), 1):
            x = self.output[i]
            j = i - 1
            while j >= 0 and self.output[j] > x:
                self.output[j+1] = self.output[j]
                j = j - 1
            self.output[j+1] = x
        stop = time.perf_counter()

        return (stop-start)
