from auxiliaries.ScalingExperiment import ScalingExperimentSpec
from insertion.insertion import InsertionSorter
from selection.selection import SelectionSorter
from merge.merge import MergeSorterTopDown
from heap.heap import HeapSorter
from quick.quick import QuickSorter
from bucket.bucket import BucketSorter

import matplotlib.pyplot as plt

spec = ScalingExperimentSpec(64, 2, 1, 1, 1)
results = []

print("Insertion Sort")
insertionSorter = InsertionSorter()
insertionResults = insertionSorter.runScalingExperiment(spec)
print(f"Array sorted? {insertionSorter.checkSorting()}")
insertionResults.summarize()
results.append([insertionResults, "Insertion"])

print("\nSelection Sort")
selectionSorter = SelectionSorter()
selectionResults = selectionSorter.runScalingExperiment(spec)
print(f"Array sorted? {selectionSorter.checkSorting()}")
selectionResults.summarize()
results.append([selectionResults, "Selection"])

print("\nMerge Sort, Top-Down")
mergeTopDownSorter = MergeSorterTopDown()
mergeTopDownResults = mergeTopDownSorter.runScalingExperiment(spec)
print(f"Array sorted? {mergeTopDownSorter.checkSorting()}")
mergeTopDownResults.summarize()
results.append([mergeTopDownResults, "Merge"])

print("\nHeap Sort")
heapSorter = HeapSorter()
heapResults = heapSorter.runScalingExperiment(spec)
print(f"Array sorted? {heapSorter.checkSorting()}")
heapResults.summarize()
results.append([heapResults, "Heap"])

print("\nQuick Sort")
quickSorter = QuickSorter()
quickResults = quickSorter.runScalingExperiment(spec)
print(f"Array sorted? {quickSorter.checkSorting()}")
quickResults.summarize()
results.append([quickResults, "Quick"])

print("\nBucket Sort")
bucketSorter = BucketSorter()
bucketResults = bucketSorter.runScalingExperiment(spec)
print(f"Array sorted? {bucketSorter.checkSorting()}")
bucketResults.summarize()
results.append([bucketResults, "Bucket"])

plt.figure()
for result in results:
    plt.plot(result[0].arraySizes, result[0].avgAvg, label=result[1])
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.xlabel("Array size", fontsize=14)
plt.ylabel("Average time to sort", fontsize=14)
plt.show()