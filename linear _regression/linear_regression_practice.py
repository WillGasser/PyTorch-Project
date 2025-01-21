import numpy as np
import csv

# Glossary:
# 1 crime_rate: Per capita crime rate by town
# 2 residential_zone: Proportion of residential land zoned for lots over 25,000 sq. ft.
# 3 non_retail_business_acre: Proportion of non-retail business acres per town
# 4 charles_river: Dummy variable indicating if the tract bounds the Charles River (1 if yes, 0 otherwise)
# 5 nitric_oxide_concentration: Concentration of nitric oxides (parts per 10 million)
# 6 average_rooms: Average number of rooms per dwelling
# 7 age: Proportion of owner-occupied units built prior to 1940
# 8 distance_to_employment_centers: Weighted distances to five Boston employment centers
# 9 radial_highways_access: Index of accessibility to radial highways
# 10 tax_rate: Full-value property-tax rate per $10,000
# 11 pupil_teacher_ratio: Pupil-teacher ratio by town
# 12 proportion_black: Proportion of the population that is African American
# 13 lower_status_population: Percentage of the population with lower socioeconomic status
# 14 median_value: Median value of owner-occupied homes in $1000s (target variable)

class Linear_Regression():
    def __init__(self, fileName: str) -> None:
        self.fileName = fileName
        # Include the intercept term (w0)
        self.w0, self.w1, self.w2 = np.random.randn(), np.random.randn(), np.random.randn()
    
    def buildData(self) -> None:
        with open(self.fileName, 'r') as file:
            data = []
            reader = csv.reader(file, delimiter=',')
            i = 0
            for row in reader:
                if i == 0:
                    i += 1
                    continue
                data.append(row)
            self.data = data
            self.training_examples = len(data)

    def hypothesis(self, x1: float, x2: float) -> float:
        return self.w0 + self.w1 * x1 + self.w2 * x2
    
    def gradient_descent(self, learning_rate: float, iterations: int) -> None:
        for _ in range(iterations):
            # Initialize gradients for w0, w1, w2
            w0_gradient, w1_gradient, w2_gradient = 0.0, 0.0, 0.0
            for row in self.data:
                x1, x2 = float(row[6]), float(row[10])
                y = float(row[14])
                y_pred = self.hypothesis(x1, x2)
                
                # (y_pred - y) is the error
                error = y_pred - y
                
                # Gradients
                # w0_gradient sums (error * 1) because x0 = 1 for the intercept
                w0_gradient += error
                w1_gradient += error * x1
                w2_gradient += error * x2

            # Update weights
            self.w0 -= (learning_rate / self.training_examples) * w0_gradient
            self.w1 -= (learning_rate / self.training_examples) * w1_gradient
            self.w2 -= (learning_rate / self.training_examples) * w2_gradient
        
    def calculate_accuracy(self) -> None:
        total_error = 0
        for i in range(self.training_examples):
            row = self.data[i]
            x1, x2 = float(row[6]), float(row[10])
            y_true = float(row[14])
            y_pred = self.hypothesis(x1, x2)
            error = abs((y_true - y_pred) / y_true) * 100
            total_error += error

        average_error = total_error / self.training_examples
        accuracy = 100 - average_error
        print(f"Accuracy: {accuracy:.2f}%")

# Example usage:
# test = Linear_Regression('Boston.csv')
# test.buildData()
# test.gradient_descent(0.00001, 10000)
# test.calculate_accuracy(1000)
