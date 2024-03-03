import json

def load_turing_machine(filename):
    with open(filename, 'r') as file:
        machine = json.load(file)
    return machine

def run_test(machine, test_input):
    tape = ['_'] * 1000  # Inicializa a fita com espaços em branco
    tape_pos = 500  # Posição inicial da cabeça de leitura/escrita
    current_state = machine["initial"]

    for symbol in test_input:
        tape[tape_pos] = symbol
        transition_found = False

        for transition in machine["transitions"]:
            if transition["from"] == current_state and transition["read"] == symbol:
                tape[tape_pos] = transition["write"]
                current_state = transition["to"]
                tape_pos += 1 if transition["dir"] == "R" else -1
                transition_found = True
                break

        if not transition_found:
            return tape, 0

    return tape, 1 if current_state in machine["final"] else 0

def main(machine_file, test_input_file):
    machine = load_turing_machine(machine_file)

    with open(test_input_file, 'r') as test_input_file:
        test_input = test_input_file.read().strip()

    tape_content, result = run_test(machine, test_input)

    print(f"Resultado: {result}")

    with open("saida.txt", 'w') as output_file:
        output_file.write("".join(tape_content).strip('_'))

if __name__ == "__main__":
    machine_file = "Duplo.json"
    test_input_file = "entrada.txt"
    main(machine_file, test_input_file)
