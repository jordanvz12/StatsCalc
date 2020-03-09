import random

def simpleRandomSample(population, numSelect):
    sampleList = []
    random.shuffle(population)
    sampleList = random.sample(population, numSelect)
    return sampleList

