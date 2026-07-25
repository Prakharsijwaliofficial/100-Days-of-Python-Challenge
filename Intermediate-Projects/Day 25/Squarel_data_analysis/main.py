import pandas

data = pandas.read_csv("Squarel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260724.csv")

Grey_squarrels = len(data[data["Primary Fur Color"] == "Gray"])

red_squarrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squarrels = len(data[data["Primary Fur Color"] == "Black"])



data_dict = {
    "Fur color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [Grey_squarrels, red_squarrels, black_squarrels]

}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")
