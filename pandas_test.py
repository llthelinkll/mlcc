import pandas as pd
import matplotlib.pyplot as plt

pd.__version__

print("=== CREATE SERIES ===")
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento','Thai'])
population = pd.Series([852469, 1015785, 12213,123123])

# this is DataFrame
print("=== CREATE DATAFRAME ===")
print(repr(pd.DataFrame({ 'City name': city_names, 'Population': population })))
print(type(pd.DataFrame({ 'City name': city_names, 'Population': population })))

# this is DataFrame also
print("=== READ FROM CSV ===")
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(repr(california_housing_dataframe.describe()))
print(type(california_housing_dataframe))

# display a few records from DataFrame
print("=== HEAD ===")
print(repr(california_housing_dataframe.head()))

# show histogram
print("=== HISTOGRAM ===")
california_housing_dataframe.hist('housing_median_age')
plt.show()

# accessing data
print("=== ACESSING DATA ===")
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
print(cities['City name'])

print(type(cities['City name'][1]))
print(cities['City name'][1])

print(type(cities[0:2]))
print(cities[0:2])

print("=== MANIPULATING DATA ====")
print((population / 1000))

print("=== MANIPULATING DATA BY NUMPY ====")
import numpy as np
print(np.log(population))

print("=== MANIPULATING DATA BY LAMBDA ====")
print(population.apply(lambda val: val > 1000000))

print("=== MANIPULATING DATA BY THEM SELF ====")
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92,100.0])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

print("=== INDEXING ====")
print(cities.index)
print(cities)
print(cities.reindex([2, 0, 1]))
print(cities.index)
print(cities)
# random
print(cities.reindex(np.random.permutation(cities.index)))