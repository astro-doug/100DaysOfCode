import pandas
from pandas import DataFrame
from pandas import Series
from typing import Final

INPUT_DATA_FILE: Final[str] = "2018_Central_Park_Squirrel_Census.csv"
OUTPUT_DATA_FILE: Final[str] = "2018_Squirrel_Color_Count.csv"
FUR_COLOR_COLUMN: Final[str] = "Primary Fur Color"


def main() -> None:
    data: DataFrame = pandas.read_csv(INPUT_DATA_FILE)
    fur_colors: list[str] = data[FUR_COLOR_COLUMN].unique()
    print(fur_colors)
    # color_count: dict[str, list[str],str, list[int]] = {}
    color_count = {}
    count_list: list = []
    for fur_color in fur_colors:
        color_list: list[str] = data[data[FUR_COLOR_COLUMN] == fur_color]
        count = len(color_list)
        count_list.append(count)
    color_count["Fur Colors"] = fur_colors
    color_count["Count"] = count_list
    print(color_count)

    output: DataFrame = DataFrame(data=color_count)
    output.to_csv(OUTPUT_DATA_FILE)
    print(output)


if __name__ == '__main__':
    main()
