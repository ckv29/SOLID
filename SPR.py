class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
        
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        return self.count
        
    def remove_entry(self, index):
        del self.entries[index]
        
    def __str__(self):
        return "\n".join(self.entries)
        
    # Методы, нарушающие SRP
    

class JournalPersitence:
    @staticmethod
    def save(journal : Journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))

    @staticmethod        
    def load(journal : Journal, filename):
        with open(filename, 'r') as file:
            journal.entries = file.readlines()
    @staticmethod        
    def load_from_web(journal : Journal, uri):
        # Здесь был бы код для загрузки из интернета
        pass
