from src import converters as module_to_test


class TestConverter:
    def test_converter_case1(self):
        test_value = '13.14%'
        actual = module_to_test.convert_percentage_as_string_to_float(test_value)
        excepted = 13.14
        assert actual == excepted
    
    def test_converter_case2(self):
        test_value = '0.1%'
        actual = module_to_test.convert_percentage_as_string_to_float(test_value)
        excepted = 0.1
        assert actual == excepted