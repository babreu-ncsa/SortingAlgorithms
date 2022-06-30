from auxiliaries.ScalingExperiment import ScalingExperimentSpec
from insertion.insertion import InsertionSorter

sorter = InsertionSorter()
spec = ScalingExperimentSpec(64, 2, 4, 25, 100)
results = sorter.runScalingExperiment(spec)

print(f"Array sizes: {results.arraySizes}")

print(f"\n\nAverage iterations: {results.avgAvg} +- {results.avgStd}")
print(f"Quickest iterations: {results.bestAvg} +- {results.bestStd}")
print(f"Slowest iterations: {results.worstAvg} +- {results.worstStd}")