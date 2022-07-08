###
# File: heap.py
# Description: Heap sort
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Friday, 8th July 2022, 11:29:54 am
# Last Modified: Friday, 8th July 2022, 1:23:16 pm
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

class HeapSorter(Sorter):

    def sortArray(self):
        """
        Sorts array using Heap Sort
        https://en.wikipedia.org/wiki/Heapsort
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
        self.output = self.heapify(self.output)
        end = self.arraySize - 1
        while end > 0:
            self.output = self.swap(self.output, end, 0)
            end = end - 1
            self.output = self.siftDown(self.output, 0, end)
        stop = time.perf_counter()

        return (stop-start)

    def parentIdx(self,idx):
        """
        Returns the parent index of an array in heap order.
        """
        return math.floor((idx-1)/2)

    def leftChildIdx(self,idx):
        """
        Returns the index of the left child of an array element in heap order.
        """
        return (2*idx + 1)

    def rightChildIdx(self,idx):
        """
        Returns the index of the right child of an array element in heap order.
        """
        return (2*idx + 2)

    def heapify(self,array):
        """
        Put elements of array in heap order.
        """
        start = self.parentIdx(array.size - 1)
        while start >= 0:
            array = self.siftDown(array, start, array.size-1)
            start = start - 1

        return array

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

    def siftDown(self,array,start,end):
        """
        Repair heap order.
        """
        sifted = array
        root = start

        while self.leftChildIdx(root) <= end:
            child = self.leftChildIdx(root)
            swap = root

            if sifted[swap] < sifted[child]:
                swap = child
            if ((child+1) <= end) and (sifted[swap] < sifted[child+1]):
                swap = child + 1
            if swap == root:
                break
            else:
                sifted = self.swap(sifted, root, swap)
                root = swap

        return sifted
