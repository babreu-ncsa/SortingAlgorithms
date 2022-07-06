from auxiliaries.ScalingExperiment import ScalingExperimentSpec
from insertion.insertion import InsertionSorter
from selection.selection import SelectionSorter

spec = ScalingExperimentSpec(8, 2, 4, 25, 100)

print("Insertion Sort")
insertionSorter = InsertionSorter()
insertionResults = insertionSorter.runScalingExperiment(spec)
print(f"Array sorted? {insertionSorter.checkSorting()}")
insertionResults.summarize()

print("\nSelection Sort")
selectionSorter = SelectionSorter()
selectionResults = selectionSorter.runScalingExperiment(spec)
print(f"Array sorted? {selectionSorter.checkSorting()}")
selectionResults.summarize()