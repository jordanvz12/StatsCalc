from Calculator.Calculator import division
from Calculator.Calculator import power
from Calculator.Calculator import product
from Calculator.Calculator import subtraction
from PopulationSampling.MarginError import margin_error
from PopulationSampling.ProbabilityTest import normalProbabilityDensity
#z value is on z table****
#formula for cohrans sample size = https://www.quora.com/What-is-Cochrans-formula
def sampleSize(data, proportion):
    denominator = power(margin_error(data, sample_size=10), 2)
    q = subtraction(1.0, proportion)
    half_numerator = product(proportion, q)
    z = normalProbabilityDensity(denominator)
    numerator = product(power(z, 2), half_numerator)
    n = division(numerator, denominator)
    return n

