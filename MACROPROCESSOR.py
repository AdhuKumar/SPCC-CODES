class MacroProcessor:
    def __init__(self):
        self.macros = {}

    def define_macro(self, macro_name, macro_body):
        self.macros[macro_name] = macro_body

    def expand_macros(self, source_code):
        for macro_name, macro_body in self.macros.items():
            source_code = source_code.replace(macro_name, macro_body)

        return source_code

if __name__ == "__main__":
    macro_processor = MacroProcessor()

    # Define a macro for printing a message
    macro_processor.define_macro("PRINT_MESSAGE", "print('Hello, world!')")

    # Define a macro for calculating the sum of two numbers
    macro_processor.define_macro("SUM", "def sum(a, b):\n  return a + b\n")

    # Define a macro for swapping two numbers
    macro_processor.define_macro("SWAP", "def swap(a, b):\n  temp = a\n  a = b\n  b = temp\n")

    # Example usage of the macros
    source_code = """
    PRINT_MESSAGE
    sum = SUM(10, 20)
    print('Sum:', sum)
    a = 5
    b = 10
    SWAP(a, b)
    print('a:', a)
    print('b:', b)
    """

    expanded_source_code = macro_processor.expand_macros(source_code)
    print(expanded_source_code)
