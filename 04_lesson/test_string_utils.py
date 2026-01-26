import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для метода capitalize

def test_capitalize_normal(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"

def test_capitalize_empty_string(string_utils):
    assert string_utils.capitalize("") == ""

def test_capitalize_single_char(string_utils):
    assert string_utils.capitalize("a") == "A"

def test_capitalize_whitespace_only(string_utils):
    assert string_utils.capitalize("   ") == "   "

def test_capitalize_number_string(string_utils):
    assert string_utils.capitalize("123abc") == "123abc"

def test_capitalize_none(string_utils):
    with pytest.raises(TypeError):
        string_utils.capitalize(None)

# Тесты для метода trim

def test_trim_normal(string_utils):
    assert string_utils.trim("   skypro") == "skypro"

def test_trim_no_leading_whitespace(string_utils):
    assert string_utils.trim("skypro") == "skypro"

def test_trim_empty_string(string_utils):
    assert string_utils.trim("") == ""

def test_trim_whitespace_only(string_utils):
    assert string_utils.trim("     ") == ""

def test_trim_trailing_whitespace(string_utils):
    assert string_utils.trim("   skypro   ") == "skypro   "

def test_trim_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# Тесты для метода contains

def test_contains_found(string_utils):
    assert string_utils.contains("SkyPro", "S") is True

def test_contains_not_found(string_utils):
    assert string_utils.contains("SkyPro", "U") is False

def test_contains_empty_string(string_utils):
    assert string_utils.contains("", "a") is False

def test_contains_empty_symbol(string_utils):
    # В Python пустая строка всегда «содержится» в любой строке
    assert string_utils.contains("abc", "") is True

def test_contains_symbol_longer_than_string(string_utils):
    assert string_utils.contains("a", "abc") is False

def test_contains_none_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")

def test_contains_none_symbol(string_utils):
    with pytest.raises(TypeError):
        string_utils.contains("abc", None)

# Тесты для метода delete_symbol

def test_delete_symbol_normal(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_substring(string_utils):
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_not_present(string_utils):
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"

def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "a") == ""

def test_delete_symbol_empty_symbol(string_utils):
    assert string_utils.delete_symbol("abc", "") == "abc"

def test_delete_symbol_all_chars(string_utils):
    assert string_utils.delete_symbol("aaaa", "a") == ""

def test_delete_symbol_none_string(string_utils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")

def test_delete_symbol_none_symbol(string_utils):
    with pytest.raises(TypeError):
        string_utils.delete_symbol("abc", None)
