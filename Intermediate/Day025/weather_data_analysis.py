import csv
import pandas
from pandas import DataFrame
from pandas import Series


def main() -> None:
    # use the built-in CSV library to read the CSV and grab the data out of a single column
    with open("weather_data.csv", mode="r") as weather_data_file:
        # data: list[str] = weather_data_file.readlines()
        data: list = list(csv.reader(weather_data_file))
        temps: list[int] = []
        for row in data[1:]: # slice off the first row to get rid of the header
            print(row)
            temps.append(int(row[1]))

    print(temps)
    print("--------------------------------------")
    # use Pandas library
    data: DataFrame = pandas.read_csv("weather_data.csv")
    print(data)
    print(data["temp"])
    temp_list: list[int] = data["temp"].to_list()
    temp_total: float = 0
    # below can also be done with sum(temp_list)
    for temp in temp_list:
        temp_total += temp
    avg_temp: float = temp_total / len(temp_list)
    print(f"Average temperature: {avg_temp:.2f}")
    print(f"Average temperature: {data["temp"].mean():.2f}")
    print(f"Max temperature: {data["temp"].max()}")

    print(data[data["day"] == "Monday"])
    # print the row with the highest temp
    print(data[data["temp"] == data["temp"].max()])

    monday: list = data[data["day"] == "Monday"]
    monday_temp: int = monday["temp"][0]
    print(f"{monday_temp}C = {(monday_temp * 9 / 5) + 32}F")


if __name__ == '__main__':
    main()
