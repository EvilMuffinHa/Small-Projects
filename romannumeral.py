#Roman numeral converter
import sys

def convert(roman_numeral):
    vals = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
    indian_numeral = 0
    for i in range(len(roman_numeral)):
        if i > 0 and vals[roman_numeral[i].lower()] > vals[roman_numeral[i - 1].lower()]:
            indian_numeral += vals[roman_numeral[i].lower()] - 2* vals[roman_numeral[i - 1].lower()]
        else:
            indian_numeral += vals[roman_numeral[i].lower()]
    return indian_numeral


if __name__ == '__main__':
    indian_numeral_list = []
    for i in range(len(sys.argv)):
        if i != 0:
            indian_numeral_list.append(convert(sys.argv[i]))
    for i in indian_numeral_list:
        print(i, end=' ')
    print('\n')
