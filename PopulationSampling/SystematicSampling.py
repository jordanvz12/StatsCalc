import random
from Calculator.Division import division



def systematicSampling(data, sample_size):
    num_values = sum(data)
    samplingInterval = num_values // sample_size
    sampleData = []
    sliceObj = slice(0, 99, samplingInterval)
    newSampleData = sampleData[sliceObj]
    return newSampleData
    #for values in data:
        #samplingInterval