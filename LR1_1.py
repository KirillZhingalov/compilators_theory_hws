def check_sequence(s: str = '') -> bool:
    state = False
    for char in s:
        if char not in ['1','0']: 
            raise AttributeError('Wrong element in sequence')
        elif char == '1': state = True
    return state

if __name__ == '__main__':
    print('LR1 task 1')
    print('Программа конечного распознавателя для языка, состоящего из 0 и 1, где имеется по крайней мере одна 1')
    input_string = input()
    if not check_sequence(input_string): print('Wrong sequence')
    else: print('Right sequence')
