# import csv

# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     for row in data:
#         print(row)






# import pandas

# data=pandas.read_csv("weather_data.csv")
# print(data.a)
# print(data[data.a==data.a.max()])


# import pandas

# data_dict={
#     "students":["suraj","rangu","pinta"],
#     "scores":[33,3,3]
# }
# data=pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")


import pandas

data=pandas.read_csv("squirrel_data.csv")
grey_sq=len(data[data["Primary Fur Color"]== "Gray"])
red_sq=len(data[data["Primary Fur Color"]== "Cinnamon"])
black_sq=len(data[data["Primary Fur Color"]== "Black"])
print(grey_sq)
print(red_sq)
print(black_sq)


data_dict={
    "Fur color":["Grey","Cinnamon","Black"],
    "Count":[grey_sq,red_sq,black_sq]
}
print(data_dict)

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")