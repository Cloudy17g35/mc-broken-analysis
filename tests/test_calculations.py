from src import calculations as module_to_test

class TestCalculations:
    def test_calculation_case1(self):
        test_value_revenue = 53348
        test_value_percentage = 12.87
        actual = module_to_test.calculate_lost_revenue(
            revenue=test_value_revenue,
            percentage_of_broken_machines=test_value_percentage
        )
        excepted = 6865.8876
        assert actual == excepted