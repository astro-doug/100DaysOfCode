def main() -> None:
    numbers: list[int] = list(range(11))

    squared_numbers: list[int] = [n**2 for n in numbers]
    only_even_numbers: list[int] =[n for n in numbers if n%2 == 0]
    print(squared_numbers)
    print(only_even_numbers)

    with open("file1.txt", "r") as file1:
        file1_data = file1.read().splitlines()
    with open("file2.txt", "r") as file2:
        file2_data = file2.read().splitlines()

    # print(file1_data)
    # print(file2_data)

    result = [int(num) for num in file1_data if num in file2_data]

    print(result)

    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22,
                 "Sunday": 24}

    weather_f = {day: (temp_c * 9 / 5 + 32) for (day, temp_c) in weather_c.items()}

    print(weather_f)

if __name__ == '__main__':
    main()
