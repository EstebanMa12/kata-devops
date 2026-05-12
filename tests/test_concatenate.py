import pytest
from src.concatenate import concatenate_nth_letters


class TestConcatenate:
    def test_example_case(self):
        assert concatenate_nth_letters(["yoda", "best", "has"]) == "yes"

    def test_empty_array(self):
        assert concatenate_nth_letters([]) == ""

    def test_single_word(self):
        assert concatenate_nth_letters(["hello"]) == "h"

    def test_words_with_varying_lengths(self):
        assert concatenate_nth_letters(["a", "ab", "abc"]) == "abc"

    def test_word_shorter_than_index(self):
        assert concatenate_nth_letters(["abc", "a", "ab"]) == "a"

    def test_tuple_accepted(self):
        assert concatenate_nth_letters(("yoda", "best", "has")) == "yes"

    def test_non_string_elements_skipped(self):
        assert concatenate_nth_letters(["yoda", 42, "has"]) == "ys"

    def test_none_element_skipped(self):
        assert concatenate_nth_letters(["x", None, "abc"]) == "xc"

    def test_words_none_raises(self):
        with pytest.raises(TypeError):
            concatenate_nth_letters(None)

    def test_string_as_container_rejected(self):
        with pytest.raises(TypeError):
            concatenate_nth_letters("yoda")

    def test_invalid_container_raises(self):
        with pytest.raises(TypeError):
            concatenate_nth_letters({0: "x"})
