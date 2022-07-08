from auxiliaries.ScalingExperiment import ScalingExperimentSpec
from insertion.insertion import InsertionSorter
from selection.selection import SelectionSorter
from merge.merge import MergeSorterTopDown

import matplotlib.pyplot as plt

spec = ScalingExperimentSpec(8, 2, 2, 25, 10)
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

#plt.figure()
#for result in results:
#    plt.plot(result[0].arraySizes, result[0].avgAvg, label=result[1])
#plt.xscale("log")
#plt.yscale("log")
#plt.legend()
#plt.xlabel("Array size", fontsize=14)
#plt.ylabel("Average time to sort", fontsize=14)
#plt.show()