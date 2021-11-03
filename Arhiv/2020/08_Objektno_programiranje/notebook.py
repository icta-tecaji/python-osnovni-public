import sys


class Note:
    def __init__(self, note_id, text, tags=""):
        self.note_id = note_id
        self.text = text
        self.tags = tags

    def match(self, string_filter):
        return string_filter in self.text or string_filter in self.tags


class Notebook:
    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []
        self._last_id = 1

    def new_note(self, text, tags=""):
        """Create a new note and add it to the list."""
        self.notes.append(Note(self._last_id, text, tags))
        self._last_id += 1

    def modify_text(self, note_id, text):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self.__find_note(note_id)
        if note:
            note.text = text
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        note = self.__find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter_string):
        """Find all notes that match the given filter
        string."""
        return [note for note in self.notes if note.match(filter_string)]

    def __find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.note_id) == str(note_id):
                return note
        return None


class NotebookMenuTerminal:
    def __init__(self) -> None:
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
            Notebook menu:
                1. Show all Notes
                2. Search Notes
                3. Add Note
                4. Modify Note
                5. Quit
            """
        )

    def run(self):
        while True:
            self.display_menu()
            chioce = input("Enter an option: ")
            action = self.choices.get(chioce)
            if action:
                action()
            else:
                print(f"{chioce} is not a valid choice.")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"**-------------------- ID: {note.note_id} --------------------**")
            print(f"Tags: {note.tags}\nText: {note.text}")

    def search_notes(self):
        string_filter = input("Search for: ")
        notes = self.notebook.search(string_filter)
        self.show_notes(notes)

    def add_note(self):
        text = input("Enter a note: ")
        tags = input("Enter tags for a note: ")
        self.notebook.new_note(text, tags)
        print("Your note was added.")

    def modify_note(self):
        note_id = input("Enter a note id: ")
        text = input("Enter text for a note: ")
        tags = input("Enter tags: ")
        if text:
            status = self.notebook.modify_text(note_id, text)
        if tags:
            status = self.notebook.modify_tags(note_id, tags)
        if not status:
            print(f"{note_id} is not a valid ID!")

    def quit(self):
        print("Hvala za uporabno našega programa.")
        sys.exit(0)


if __name__ == "__main__":
    notebook_menu = NotebookMenuTerminal()
    notebook_menu.run()
