from Calculator.Calculator import division
from Calculator.Calculator import product
from Calculator.Calculator import power
from PopulationSampling.ProbabilityTest import normalProbabilityDensity
from Statistics.Statistics import standard_deviation
def samplesizeKnownPop(data, confidence, error):
    z = division(confidence, 2)
    ztable_value = normalProbabilityDensity(z)
    standardDeviation = standard_deviation(data)
    ztableTimesStandard = product(ztable_value, standardDeviation)
    nextStep = division(ztableTimesStandard, error)
    sample_size = power(nextStep, 2)
    return sample_size


