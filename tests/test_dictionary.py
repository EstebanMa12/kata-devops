import pytest

from src.dictionary import Dictionary


class TestDictionary:
    def test_look_existing_word(self):
        dictionary = Dictionary()
        dictionary.newentry("hello", "a greeting")
        assert dictionary.look("hello") == "a greeting"

    def test_look_non_existing_word(self):
        dictionary = Dictionary()
        assert dictionary.look("hello") == "Not found"

    def test_getallwords(self):
        dictionary = Dictionary()
        dictionary.newentry("hello", "a greeting")
        assert dictionary.getallwords() == {"hello": "a greeting"}

    def test_multiple_entries(self):
        dictionary = Dictionary()
        dictionary.newentry("hello", "a greeting")
        dictionary.newentry("world", "a greeting")
        assert dictionary.getallwords() == {
            "hello": "a greeting",
            "world": "a greeting",
        }

    def test_overwrite_entry(self):
        dictionary = Dictionary()
        dictionary.newentry("hello", "a greeting")
        dictionary.newentry("hello", "a new greeting")
        assert dictionary.look("hello") == "a new greeting"

    def test_getallwords_empty(self):
        dictionary = Dictionary()
        assert dictionary.getallwords() == {}

    def test_invalid_word(self):
        dictionary = Dictionary()
        assert dictionary.look("123") == "Not found"

    def test_newentry_rejects_non_str(self):
        dictionary = Dictionary()
        with pytest.raises(TypeError):
            dictionary.newentry(123, "a greeting")
        with pytest.raises(TypeError):
            dictionary.newentry("hello", None)

    def test_look_rejects_non_str(self):
        dictionary = Dictionary()
        with pytest.raises(TypeError):
            dictionary.look(123)

    def test_getallwords_returns_copy(self):
        dictionary = Dictionary()
        dictionary.newentry("hello", "a greeting")
        snapshot = dictionary.getallwords()
        snapshot["extra"] = "leak"
        assert dictionary.getallwords() == {"hello": "a greeting"}

    def test_empty_string_entry(self):
        dictionary = Dictionary()
        dictionary.newentry("", "empty key")
        assert dictionary.look("") == "empty key"