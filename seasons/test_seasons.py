from datetime import date
from seasons import Season, main
from seasons import num_to_word
import pytest

@pytest.fixture
def mock_date(mocker):
    mocked_date = mocker.patch("seasons.date", autospec=True)
    mocked_date.today.return_value = date(2025, 9, 21)
    mocked_date.fromisoformat.side_effect = date.fromisoformat
    return mocked_date 

valid_cases = [       
    ("1999-01-01", 14054400),
    ("2005-01-01", 10897920),
    ("2011-01-01", 7742880)
                    ]
@pytest.mark.parametrize("birth_date_str, expected_minutes", valid_cases)
def test_specific_years(mock_date, birth_date_str, expected_minutes):
    ob = Season(birth_date_str)
    assert ob.str_to_minute() == expected_minutes



invalid_date_cases = [
    "January 1, 1999",      
    "1999/01/01",          
    "1-1-1999",           
    "2023-13-01",        
    "cat",              
]

@pytest.mark.parametrize("invalid_input", invalid_date_cases)
def test_invalid_date_cases(mocker, invalid_input):
    mocker.patch('builtins.input', return_value=invalid_input)

    with pytest.raises(SystemExit):
        main()

conversion_test_cases = [
    (525600, "Five hundred twenty-five thousand, six hundred"),
    (1051200, "One million, fifty-one thousand, two hundred"),
    (1440, "One thousand, four hundred forty"),
    (3944160, "Three million, nine hundred forty-four thousand, one hundred sixty"),
]

@pytest.mark.parametrize("minute_in, excepted_word", conversion_test_cases)
def test_word_conversion(minute_in, excepted_word):
    assert num_to_word(minute_in) == excepted_word
