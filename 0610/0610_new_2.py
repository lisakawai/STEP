#-*- coding: utf-8 -*-

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.': #小数に対応
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMul(line, index):
    token = {'type': 'MUL'}
    return token, index + 1


def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1


def readStart(line, index):
    token = {'type': 'START'}
    return token, index + 1


def readEnd(line, index):
    token = {'type': 'END'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        elif line[index] == '(':
            (token, index) = readStart(line, index)
        elif line[index] == ')':
            (token, index) = readEnd(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    bracket_count = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'START': #　'('を見つけたら対応する')'を探し、その中を再帰関数を用いて計算する
            index_start = index
            index += 1                       
            while index < len(tokens):
                if tokens[index]['type'] == 'END':
                    if bracket_count == 0:
                        index_end = index
                        token_part = evaluate( tokens[index_start + 1: index_end] )
                        tokens.insert(index_start, {'type': 'NUMBER', 'number': token_part })
                        del tokens[index_start  + 1 : index_end + 2]
                        index = index_start
                        break 
                    else:
                        bracket_count -= 1
                elif tokens[index]['type'] == 'START':
                    bracket_count += 1
                index += 1
        index += 1
    
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MUL':
                tokens[index - 2]['number'] *= tokens[index]['number']
                del tokens[index - 1 : index + 1]
                index -= 2
            elif tokens[index - 1]['type'] == 'DIV':
                tokens[index - 2]['number'] /= float(tokens[index]['number'])
                del tokens[index - 1 : index + 1]
                index -= 2
        index += 1

    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:

    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %.3lf\n" % answer
