###
# File: bucket.py
# Description: Bucket sort
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Friday, 22nd July 2022, 2:09:09 pm
# Last Modified: Friday, 22nd July 2022, 2:45:43 pm
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
from insertion.insertion import InsertionSorter
import time
import numpy as np

class BucketSorter(Sorter):
    def sortArray(self):
        """
        Sorts array using Bucket Sort 
        https://en.wikipedia.org/wiki/Bucket_sort
        Returns:
            - time (float): elapsed time to sort the array
        Updates:
            - self.output: the sorted array
        """
        if (self.arraySize == 0):
            print("Please generate array!")
            return 0

        insertionSorter = InsertionSorter()

        start = time.perf_counter()

        bucket = []
        self.output = self.input

        for _ in range(self.arraySize):
            bucket.append([])

        for j in range(self.arraySize):
            elmnt = self.output[j]
            index = int(10 * elmnt)
            bucket[index].append(elmnt)

        for i in range(self.arraySize):
            if bucket[i]:
                insertionSorter.input = np.array(bucket[i])
                insertionSorter.arraySize = len(bucket[i])
                insertionSorter.sortArray()
                bucket[i] = list(insertionSorter.output)
        
        k = 0
        for i in range(self.arraySize):
            for j in range(len(bucket[i])):
                self.output[k] = bucket[i][j]
                k = k + 1

        stop = time.perf_counter()
        
        return (stop-start)


