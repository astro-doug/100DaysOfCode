from pandas import DataFrame
import pandas
from typing import Final

DATA_FILE: Final[str] = "nato_phonetic_alphabet.csv"


def load_alphabet_data() -> dict:
    data: DataFrame = pandas.read_csv(DATA_FILE)
    data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
    print(data_dict)
    return data_dict


def generate_nato_spelling(input_word: str, data_dict: dict) -> list:
    nato_spelling:list = [data_dict[letter] for letter in input_word]

    return nato_spelling


def main() -> None:
    data: dict = load_alphabet_data()
    input_word: str = input("Enter a word: ").upper()
    nato_spelling: list = generate_nato_spelling(input_word, data)
    print(nato_spelling)


if __name__ == '__main__':
    main()
