import json

def load_turing_machine(filename):
    with open(filename, 'r') as file:
        machine = json.load(file)
    return machine

def run_turing_machine(machine, input_word):
    tape = ['_'] * 1000  # Inicializa a fita com espaços em branco
    tape_pos = 500  # Posição inicial da cabeça de leitura/escrita
    current_state = machine["initial"]

    for symbol in input_word:
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
            return False, tape

    if current_state == 3:
        current_state = 4

    return current_state in machine["final"], tape

def main(machine_file, problem_file):
    machine = load_turing_machine(machine_file)

    with open(problem_file, 'r') as file:
        input_word = file.read().strip()

    accepted, tape = run_turing_machine(machine, input_word)

    with open("saida.txt", 'w') as output_file:
        output_file.write(''.join(tape).strip('_'))

    
    print("Resultado:", 1 if accepted else 0)

if __name__ == "__main__":
    machine_file = "Duplo.json"
    problem_file = "entrada.txt"
#problem_file = "problema.txt"
    main(machine_file, problem_file)
