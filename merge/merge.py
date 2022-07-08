###
# File: merge.py
# Description: Mergesort implementation
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 6th July 2022, 10:11:54 am
# Last Modified: Thursday, 7th July 2022, 2:41:20 pm
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
import numpy as np

class MergeSorterTopDown(Sorter):

    def sortArray(self):
        """
        Sorts array using Merge Sort
        https://en.wikipedia.org/wiki/Merge_sort

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
        lst = list(self.input)
        lst = self.mergeSort(lst)
        self.output = np.array(lst)
        stop = time.perf_counter()

        return (stop-start)


    def mergeSort(self, lst):
        """
        Splits the array that is passed as an argument and merges them in the end.
        This is recursive until the list has a single element.

        Input:
            - lst (list): the list if elements to be sorted

        Output
            - sortedLst (list): the sorted list
        """
        # this guarantees you won't go into an infinite recursion
        if (len(lst) <= 1):
            return lst

        left = []
        right = []
        for i in range(len(lst)):
            if i < len(lst) / 2:
                left.append(lst[i])
            else:
                right.append(lst[i])


        left = self.mergeSort(left)
        right = self.mergeSort(right)

        return self.merge(left, right)

    def merge(self, lst1, lst2):
        """
        Given two lists, iterate over them and sort them using Merge Sort.
        
        Inputs:
            - lst1 (list): the first list
            - lst2 (list): the second lust

        Returns:
            - result (list): the resulting merged list
        """

        result = []

        while lst1 and lst2:
            if lst1[0] <= lst2[0]:
                result.append(lst1[0])
                lst1.pop(0)
            else:
                result.append(lst2[0])
                lst2.pop(0)

        while lst1:
            result.append(lst1[0])
            lst1.pop(0)
        while lst2:
            result.append(lst2[0])
            lst2.pop(0)

        return result
