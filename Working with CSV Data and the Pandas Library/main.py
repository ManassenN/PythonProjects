import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# average = float(sum(temp_list)/len(temp_list))
# print(average) 

# print(data["temp"].max())
# print(data.condition)

# print(data[data.temp == data.temp.max()])

# Create dataframe from scratch
data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores": [76,56,100]
}
data = pandas.DataFrame(data_dict)
print(data)