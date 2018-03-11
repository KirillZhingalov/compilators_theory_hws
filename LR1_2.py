def create_dct() -> dict:
    k = {}
    for i in range(4):
        k.update({
            'A'+str(i): {
                'a': 'B'+str(i),
                'b': 'E'+str(i),
                'c': 'H'+str(i),
                'd': 'H'+str(i),
                'e': 'H'+str(i),
            },
            'B'+str(i): {
                'a': 'C'+str(i),
                'b': 'C'+str(i),
                'c': 'C'+str(i),
                'd': 'C'+str(i),
                'e': 'C'+str(i),
                'f': 'A'+str(i+1)
            },
            'C'+str(i): {
                'a': 'D'+str(i),
                'b': 'D'+str(i),
                'c': 'D'+str(i),
                'd': 'D'+str(i),
                'e': 'D'+str(i),
                'f': 'A'+str(i+1)
            },
            'D'+str(i): {
                'f': 'A'+str(i+1)
            },
            'E'+str(i): {
                'a': 'F'+str(i),
                'b': 'F'+str(i),
                'c': 'F'+str(i),
                'd': 'G'+str(i),
                'e': 'D'+str(i),
                'f': 'A'+str(i+1)
            },
            'F'+str(i): {
                'a': 'D'+str(i),
                'b': 'D'+str(i),
                'c': 'D'+str(i),
                'd': 'D'+str(i),
                'e': 'D'+str(i),
                'f': 'A'+str(i+1)
            },
            'G'+str(i): {
                'a': 'D'+str(i),
                'b': 'D'+str(i),
                'c': 'D'+str(i),
                'd': 'D'+str(i),
                'f': 'A'+str(i+1)
            },
            'H'+str(i): {
                'a': 'D'+str(i),
                'b': 'D'+str(i),
                'c': 'D'+str(i),
                'd': 'D'+str(i),
                'e': 'D'+str(i),
                'f': 'A'+str(i+1)
            }
    })
    return k


def patternRecognition(s: str, dct: dict) -> bool:
    state = 'A0'
    i = 0
    while i in range(len(s)) and state:
        word = s[i]
        try:
            symbol = int(word)
            if symbol in range(2):      symbol = 'a'
            elif symbol == 2:           symbol = 'b'
            elif symbol in range(3,5):  symbol = 'c'
            elif symbol == 5:           symbol = 'd'
            elif symbol in range(6,10): symbol = 'e'
        except:
            if word == '.':
                symbol = 'f'
            else:
                return False
        try:
            state = dct[state][symbol]
        except:
            return False
        i += 1
    if state and state in ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3']:
        return True
    return False


if __name__ == '__main__':
    string = input()
    res = patternRecognition(string, create_dct())
    if res:
        print('Successful analysis')
    else:
        print('Unsuccessful analysis')