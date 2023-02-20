import pandas
import pandas as pd


data_sq = pd.read_csv("Squirrel_Data.csv")
# data_weather = pd.read_csv("weather_data.csv")


grey_sq = len(data_sq[data_sq["Primary Fur Color"] == "Gray"])
print(f"{grey_sq} grey squarrels")

cinnamon_sq = len(data_sq[data_sq["Primary Fur Color"] == "Cinnamon"])
print(f"{cinnamon_sq} grey squarrels")

black_sq = len(data_sq[data_sq["Primary Fur Color"] == "Black"])
print(f"{black_sq} grey squarrels")

data_dict = {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [grey_sq, cinnamon_sq, black_sq]
}

df = pandas.DataFrame(data_dict)
df.to_csv("SquarrelColor_numbers")