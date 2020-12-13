"""Unit tests for the units converter library functions"""
# pylint: disable=unused-variable

# import the functions to be tested
from converters import mi2km, km2mi, g2oz, oz2g

def describe_a_library_of_units_converters():
    """Test suite for units conversion functions"""
    def blows_smoke():
        assert True

    def can_convert_mi_to_km():
        assert mi2km(5) == 1.609344 # Miles => Kilometers
        assert mi2km(10) == 16.09322 # Miles => Kilometers

    def can_convert_km_to_mi():
        assert km2mi(10) == 6.21371192 # Kilometers => Miles
        assert km2mi(3.5) == 2.17479917 # Kilometers => Miles

    def can_convert_g_to_oz():
        assert g2oz (2) == 0.07054792 # Grams => Ounces
        assert g2oz(28) == 0.98767094 # Grams => Ounces

    def can_convert_oz_to_g():
        assert oz2g (1) == 28.3495231 # Ounces => Grams
        assert oz2g (12) == 340.194277 # Ounces => Grams
