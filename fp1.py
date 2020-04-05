import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Imports data
math_data = pd.read_csv("student/student-mat.csv", sep = ";")
port_data = pd.read_csv("student/student-por.csv", sep = ";")

# Adds dummy variables for subject
math_data["Math"] = [1] * len(math_data)
math_data["Language"] = [0] * len(math_data)
port_data["Math"] = [0] * len(port_data)
port_data["Language"] = [1] * len(port_data)

# Appends data
student_data = pd.concat([math_data, port_data])

# Reads data to new data file
student_data.to_csv("student/student-all.csv")