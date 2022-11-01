from roman_numeral_converter import *
import pytest

def test_to_arabic_number_1_rta():
    """simple to_arabic_number (I) == 1"""
    assert to_arabic_number("I") == 1


def test_to_arabic_number_2008_rta():
    """multi to_arabic_number (MMVIII) == 2008"""
    assert to_arabic_number("MMVIII") == 2008


def test_to_arabic_number_4_rta():
    """simple subtraction to_arabic_number (IV) == 4"""
    assert to_arabic_number("IV") == 4


def test_to_arabic_number_90_rta():
    """subtraction to_arabic_number (XC) == 90"""
    assert to_arabic_number("XC") == 90


def test_to_arabic_number_3999_rta():
    """big to_arabic_number (MMMCMXCIX) == 3999"""
    assert to_arabic_number("MMMCMXCIX") == 3999

def test_to_roman_numeral_1_atn():
    """simple to_roman_numeral (1) == I"""
    assert to_roman_numeral(1) == "I"


def test_to_roman_numeral_2008_atn():
    """multi to_roman_numeral (2008) == MMVIII"""
    assert to_roman_numeral(2008) == "MMVIII"


def test_to_roman_numeral_4_atn():
    """simple subtraction to_roman_numeral (4) == IV"""
    assert to_roman_numeral(4) == "IV"


def test_to_roman_numeral_90_atn():
    """subtraction to_roman_numeral (90) == XC"""
    assert to_roman_numeral(90) == "XC"


def test_to_roman_numeral_3999_atn():
    """big to_roman_numeral (3999) == MMMCMXCIX"""
    assert to_roman_numeral(3999) == "MMMCMXCIX"
