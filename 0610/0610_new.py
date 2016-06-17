#-*- coding: utf-8 -*-
level_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #階層ごとの括弧の個数を保存しておく配列(level:階層、count:番号)、グローバル変数


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


def readStart(line, index, level, count):
    token = {'type': 'START', 'level': level, 'count': count}
    return token, index + 1


def readEnd(line, index, level, count):
    token = {'type': 'END', 'level': level, 'count': count}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    flag = 0   # 直前にあった括弧が"("であったか")"であったか保存しておくflag, {0 : "(" , 1 : ")"}
    stock = [] #　閉じていない括弧のlevelとcountを格納しておくリスト

    global level_count 
    level_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #個数を初期化
    
    level = -1 #　初期値
    count = 1

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
            if flag == 0: # 直前の括弧が"("だったとき
                stock.insert(0, [level,count]) #　閉じていない括弧のlevelとcountと一時的に保存
                level += 1
            level_count[level] += 1
            count = level_count[level]
            (token, index) = readStart(line, index, level, count)
            flag = 0
        elif line[index] == ')':
            if flag == 1: # 直前の括弧が")"だったとき
                level = stock[0][0] #　閉じていなかった括弧のlevelとcountを格納
                count = stock[0][1] 
                del stock[0]        #　括弧が閉じたのでこの情報は削除
            (token, index) = readEnd(line, index, level, count)
            flag = 1
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    global level_count
    index = 0
    for level in range(len(level_count)): #  levelがどこまであったか確認
        if level_count[level] == 0:
            max_level = level 
            break
    
    for i in reversed(range(max_level)): #  levelの数分だけforループ、levelが高いものから
        for j in range(1, level_count[i] + 1): #  各階層のcountの分だけ
            index = 0
            while index < len(tokens): #　括弧の最初と最後のindexを調べる
                if tokens[index]['type'] == 'START' and tokens[index]['level'] == i and tokens[index]['count'] == j:
                    start_index = index
                elif tokens[index]['type'] == 'END' and tokens[index]['level'] == i and tokens[index]['count'] == j:
                    end_index = index
                    break
                index += 1
            tokens[start_index + 1]['number'] = calculate(tokens[start_index + 1 : end_index]) #  括弧の中だけ計算
            del tokens[start_index] #　使わないリスト成分は削除
            del tokens[start_index + 1 : end_index]

    answer = calculate(tokens) #　括弧がなくなった式を計算
    return answer
    

def calculate(part): 
    part_sum = 0
    part.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 0
    while index < len(part):
        if part[index]['type'] == 'NUMBER':
            if part[index - 1]['type'] == 'MUL':
                part[index - 2]['number'] *= part[index]['number']
                del part[index - 1 : index + 1]
                index -= 2
            elif part[index - 1]['type'] == 'DIV':
                part[index - 2]['number'] /= float(part[index]['number'])
                del part[index - 1 : index + 1]
                index -= 2
        index += 1
    
    index = 0
    while index < len(part):
        if part[index]['type'] == 'NUMBER':
            if part[index - 1]['type'] == 'PLUS':
                part_sum += part[index]['number']
            elif part[index - 1]['type'] == 'MINUS':
                part_sum -= part[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return part_sum


while True:

    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %.3lf\n" % answer

