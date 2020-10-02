"""import the functions to be tested"""
from converters import gbp2usd
def describe_a_library_of_units_converters():
    """test suite for units conversion function"""
    # pylint: disable=unused-variable
    def blows_smoke():
        assert True
    def can_convert_gbp_to_usd():
        assert gbp2usd(5) == 7.968 # 5 gpd == 7.968 usd
