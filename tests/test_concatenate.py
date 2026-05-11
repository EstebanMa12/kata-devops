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
