import numpy as np
import matplotlib.pyplot as plt
import csv

boston_house_data_csv = "Boston.csv"

# Glossary:
# crime_rate: Per capita crime rate by town
# residential_zone: Proportion of residential land zoned for lots over 25,000 sq. ft.
# non_retail_business_acre: Proportion of non-retail business acres per town
# charles_river: Dummy variable indicating if the tract bounds the Charles River (1 if yes, 0 otherwise)
# nitric_oxide_concentration: Concentration of nitric oxides (parts per 10 million)
# average_rooms: Average number of rooms per dwelling
# age: Proportion of owner-occupied units built prior to 1940
# distance_to_employment_centers: Weighted distances to five Boston employment centers
# radial_highways_access: Index of accessibility to radial highways
# tax_rate: Full-value property-tax rate per $10,000
# pupil_teacher_ratio: Pupil-teacher ratio by town
# proportion_black: Proportion of the population that is African American
# lower_status_population: Percentage of the population with lower socioeconomic status
# median_value: Median value of owner-occupied homes in $1000s (target variable)



def build_data(fileName: str) -> list[list[float]]:
    with open(fileName, 'r'):
        houses = []
        reader = csv.reader(boston_house_data_csv, delimiter=',')
        for row in reader:
            houses.append(row)
        return houses
        
        
h0 =  
    


