def convert_percentage_as_string_to_float(s:str) -> float:
    without_percentage:str = s.replace('%', '')
    striped:str = without_percentage.strip()
    return float(striped)