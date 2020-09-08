import energy_landscapes
import file_reader
import sys

if __name__ == '__main__':
    f = sys.argv[1]
    output_name = sys.argv[2]
    input_dict = file_reader.read_input(f)

    N = input_dict['N']
    trials = input_dict['trials']
    cycles = input_dict['cycles']
    amplitude = input_dict['amp']
    temperature = input_dict['temp']
    L = input_dict['L']
    anneal = input_dict['anneal']
    alpha = input_dict['alpha']

    energy_landscapes.run_el(n=N, trials=trials, cycles=cycles, amplitude=amplitude, temperature=temperature,
                             L=L, output=output_name, anneal=anneal, alpha=alpha)





