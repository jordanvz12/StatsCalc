from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviation
def confidenceInterval(data):
    mean_data = mean(data)
    standardDeviation = standard_deviation(data)
    return mean_data, "=-", standardDeviation

