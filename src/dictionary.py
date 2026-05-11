class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word: str, definition: str) -> None:
        self.entries[word] = definition

    def look(self, word: str) -> str:
        return self.entries.get(word, "Not found")

    def getallwords(self) -> dict[str, str]:
        return self.entries
