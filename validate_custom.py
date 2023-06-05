
def validate_country_code(country_code):
    print(f'passed country_code = {country_code}')
    if len(country_code) != 2:
        print(f'Incorrect lenght of country_code. You typed: {country_code}')