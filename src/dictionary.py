class Dictionary:
    def __init__(self) -> None:
        self.entries: dict[str, str] = {}

    def newentry(self, word: str, definition: str) -> None:
        if not isinstance(word, str) or not isinstance(definition, str):
            raise TypeError("word and definition must be str")
        self.entries[word] = definition

    def look(self, word: str) -> str:
        if not isinstance(word, str):
            raise TypeError("word must be str")
        return self.entries.get(word, "Not found")

    def getallwords(self) -> dict[str, str]:
        return dict(self.entries)
