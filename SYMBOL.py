class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, value):
        if name in self.symbols:
            return False  # Symbol already exists
        self.symbols[name] = value
        return True

    def lookup(self, name):
        return self.symbols.get(name, None)

if __name__ == '__main__':
    symbol_table = SymbolTable()

    # Insert symbols into the table
    symbol_table.insert("x", 10)
    symbol_table.insert("y", 20)
    symbol_table.insert("z", 30)

    # Lookup symbols in the table
    print("Value of x:", symbol_table.lookup("x"))
    print("Value of y:", symbol_table.lookup("y"))
    print("Value of a:", symbol_table.lookup("a"))  # Symbol not found
