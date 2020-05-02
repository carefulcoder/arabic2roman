# pylint: disable=unused-variable
"""Unit tests for Arabic2Roman."""

from arabic2roman import convert

def describe_an_arabic2roman_program_that():
    """A program to convert Arabic numerals to Roman numerals."""

    def has_a_smoke_test():
        """Make sure our testing infrastructure is working."""
        assert True == True

def can_convert_1_to_I():
    assert convert(1) == "I"

def can_convert_2_to_II():
    assert convert(2) == "II"