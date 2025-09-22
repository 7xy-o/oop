import inflect
from datetime import date
import sys

p = inflect.engine()

def main():
    try:
        my_birthday: str = input("Date of Birth: ")
        season = Season(my_birthday).str_to_minute()
        print(f"{num_to_word(season)} minutes")
    except ValueError:
        sys.exit("Invalid date")
class Season:
    def __init__(self, birthday: str):
        self.birthday = date.fromisoformat(birthday)

    def str_to_minute(self):
        today = date.today()
        age_in_day: int = (today - self.birthday).days 
        age_in_minute: int = age_in_day * 24 * 60
        return age_in_minute

    
def num_to_word(number) -> str:
    word = (p.number_to_words(number, andword="")).capitalize()
    return word


if __name__ == "__main__":
    main()
