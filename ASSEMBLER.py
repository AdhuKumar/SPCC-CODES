class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.literal_table = {}
        self.location_counter = 0

    def pass_one(self, source_code):
        for line in source_code:
            tokens = line.split()

            if tokens[0].endswith(':'):
                label = tokens[0][:-1]
                self.symbol_table[label] = self.location_counter

            if tokens[0].startswith('.'):
                directive = tokens[0][1:]

                if directive == 'ORG':
                    self.location_counter = int(tokens[1])
                elif directive == 'DATA':
                    self.location_counter += len(tokens[1:])

                elif directive == 'EQU':
                    self.symbol_table[tokens[1]] = self.symbol_table[tokens[2]]

            if tokens[0].startswith('='):
                literal = tokens[0][1:]
                self.literal_table[literal] = self.location_counter
                self.location_counter += 1

            if tokens[0] not in {':', '.', 'START', 'END'}:
                self.location_counter += 1

    def pass_two(self, source_code):
        for line in source_code:
            tokens = line.split()

            if tokens[0] not in {':', '.', 'START', 'END'}:
                opcode = tokens[0]
                operand = None

                if len(tokens) > 1:
                    operand = tokens[1]

                machine_code = self.generate_machine_code(opcode, operand)

                if machine_code:
                    print(machine_code)

    def generate_machine_code(self, opcode: object, operand: object) -> object:
        opcodes_to_binary = dict(LDA='0001', ADD='0010', STA='0011')

        if opcode in opcodes_to_binary:
            binary_opcode = opcodes_to_binary[opcode]
            if operand is not None:
                numeric_part = ''.join(filter(str.isdigit, operand))
                binary_operand = f'{int(numeric_part):08b}'
                return f'{binary_opcode} {binary_operand}'

        return ""

if __name__ == '__main__':
    with open(r'/Users/adhukumara/VS FOLDER/SPCC/source.asm', 'r') as f:
        source_code = f.readlines()

    assembler = Assembler()

    assembler.pass_one(source_code)
    assembler.pass_two(source_code)
