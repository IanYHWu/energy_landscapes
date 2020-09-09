"""
Reads in an input file and passes data to energy_landscapes.py module
"""

def read_input(FILE):
    """Reads in a sample input file and returns a dictionary containing the inputs to be used by the main program"""

    input_dict = {'N': None,
                  'trials': None,
                  'cycles': 100000,
                  'amp': 0.1,
                  'temp': 10,
                  'L': 4,
                  'mode': 'LJ',
                  'anneal': False,
                  'alpha': 0.9999}

    with open(FILE, 'r') as lines:
        for line in lines:
            if 'PARTICLES' in line:
                input_dict['N'] = int((line.split(':')[1]).strip())
            elif 'TRIALS' in line:
                input_dict['trials'] = int((line.split(':')[1]).strip())
            elif 'CYCLES' in line:
                input_dict['cycles'] = int((line.split(':')[1]).strip())
            elif 'AMPLITUDE' in line:
                input_dict['amp'] = float((line.split(':')[1]).strip())
            elif 'TEMPERATURE' in line:
                input_dict['temp'] = float((line.split(':')[1]).strip())
            elif 'BOX_LENGTH' in line:
                input_dict['L'] = float((line.split(':')[1]).strip())
            elif 'POTENTIAL' in line:
                input_dict['mode'] = (line.split(':')[1]).strip()
            elif 'ANNEAL' in line:
                input_dict['anneal'] = True if (line.split(':')[1]).strip() == 'TRUE' else False
            elif 'ALPHA' in line:
                input_dict['alpha'] = float((line.split(':')[1]).strip())
            elif '' in line:
                pass
            else:
                raise Exception('Unknown input {}'.format(line))

    if not input_dict['N']:
        raise Exception('Missing particle count data. All input files must contain PARTICLES and TRIALS')
    if not input_dict['trials']:
        raise Exception('Missing trials data. All input files must contain PARTICLES and TRIALS')

    return input_dict
