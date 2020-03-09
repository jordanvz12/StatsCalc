from Calculator.Calculator import division
from Calculator.Calculator import subtraction
from Calculator.Calculator import product
from Calculator.Calculator import power
from PopulationSampling.ProbabilityTest import normalProbabilityDensity

def sample_size_unknown(percent, confidence, width):
    confidence_int = division(confidence, 2)
    zscore = normalProbabilityDensity(confidence_int)
    error = division(width, 2)
    p = subtraction(1, percent)
    pTimesq = product(percent, p)
    zDivideError = division(zscore, error)
    powerZdivError = power(zDivideError, 2)
    return product(pTimesq, powerZdivError)

