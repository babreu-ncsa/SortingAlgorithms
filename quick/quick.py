###
# File: quick.py
# Description: Quick sort using Lomuto partition
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Friday, 22nd July 2022, 1:03:09 pm
# Last Modified: Friday, 22nd July 2022, 1:27:35 pm
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
import math
import time

class QuickSorter(Sorter):

    def sortArray(self):
        """
        Sorts array using Quick Sort (Lomuto partition scheme)
        https://en.wikipedia.org/wiki/Quicksort
        Returns:
            - time (float): elapsed time to sort the array
        Updates:
            - self.output: the sorted array
        """
        if (self.arraySize == 0):
            print("Please generate array!")
            return 0

        start = time.perf_counter()
        self.output = self.input
        self.quicksort(self.output, 0, self.arraySize-1)
        stop = time.perf_counter()
        
        return (stop-start)


    def swap(self, array, idx1, idx2):
        """
        Swap two elements in an array.
        """
        swaped = array
        x = array[idx1]
        y = array[idx2]
        swaped[idx1] = y
        swaped[idx2] = x

        return swaped


    def partition(self, array, low, high):
        """
        Divides array into two partitions: smaller or equal than pivot, larger than pivot.
        """
        # last element is the pivot
        pivot = array[high]

        # temporary pivot index
        i = low - 1

        for j in range(low, high, 1):
            if array[j] <= pivot:
                # move temporary pivot index forward
                i = i + 1
                # swap current element with element at temporary pivot index
                array = self.swap(array, i, j)

        # move pivot element to correct pivot position
        i = i + 1
        array = self.swap(array, i, high)

        return i            


    def quicksort(self, array, low, high):
        if low >= high or low < 0:
            return
        
        # partition array
        p = self.partition(array, low, high)

        # sort the partitions
        self.quicksort(array, low, p-1)
        self.quicksort(array, p+1, high)

