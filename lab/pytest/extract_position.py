# Replace nested conditional with gaurd clauses

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                print('entire line', len(line))
                start_index = line.find('x:') + 2
                print('start idx: ', start_index)
                pos = line[start_index:] # from start_index to the end.
                print('position: ',pos)
            else: 
                pos = None
    return pos


def test_extract_position():
    assert extract_position('debug') == None 
    assert extract_position('error') == None 
    assert extract_position('|update| the positron location in the particle accelerator is x:21.432') == '21.432'
    



if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)