memory = []
registerFile = {
    '000':'0000000000000000',
    '001':'0000000000000000',
    '010':'0000000000000000',
    '011':'0000000000000000',
    '100':'0000000000000000',
    '101':'0000000000000000',
    '110':'0000000000000000',
    '111':'0000000000000000',
}
programCounter = 0

instructiontypes = {
    '00000': 'A',
    '00001': 'A',
    '00110': 'A',
    '01010': 'A',
    '01011': 'A',
    '01100': 'A',
    '00010': 'B',
    '01000': 'B',
    '01001': 'B',
    '00011': 'C',
    '00111': 'C',
    '01101': 'C',
    '01110': 'C',
    '00100': 'D',
    '00101': 'D',
    '01111': 'E',
    '10000': 'E',
    '10001': 'E',
    '10010': 'E',
    '10011': 'F',
}

def executionEngine(instruction):
    global programCounter
    opcode = instruction[0:5]
    type = instructiontypes[opcode]
    if type == 'A':
        reg1 = instruction[7:10]
        reg2=instruction[10:13]
        reg3=instruction[13:16]
        if opcode == '00000':  #add
            sum = int(registerFile[reg2], 2) + int(registerFile[reg3], 2)
            sum = format(sum, 'b')
            temp = ''
            while len(temp) < 16 - len(sum):
                temp += '0'
            sum = temp + sum
            registerFile[reg1] = sum
        elif opcode == '00001':  #sub
            diff = int(registerFile[reg2], 2) - int(registerFile[reg3], 2)
            diff = format(diff, 'b')
            temp = ''
            while len(temp) < 16 - len(diff):
                temp += '0'
            diff = temp + diff
            registerFile[reg1] = diff
        elif opcode == '00110':  #mul
            prod = int(registerFile[reg2], 2) - int(registerFile[reg3], 2)
            prod = format(prod, 'b')
            temp = ''
            while len(temp) < 16 - len(prod):
                temp += '0'
            prod = temp + prod
            registerFile[reg1] = prod
        elif opcode == '01010':
            registerFile[reg1] = ''
            for i in range(16):
                registerFile[reg1] += registerFile[reg2][i] ^ registerFile[reg3][i]
        elif opcode == '01011':
            registerFile[reg1] = ''
            for i in range(16):
                registerFile[reg1] += registerFile[reg2][i] | registerFile[reg3][i]
        elif opcode == '01100':
            registerFile[reg1] = ''
            for i in range(16):
                registerFile[reg1] += registerFile[reg2][i] & registerFile[reg3][i]
    elif type == 'B':
        reg = instruction[5:8]
        val = instruction[8:16]
        if opcode == '00010':  #mov
            while len(val) < 16:
                val = '0' + val
            registerFile[reg] = val
    elif type == 'C':
        reg1 = instruction[10:13]
        reg2 = instruction[13:16]
        if opcode == '00011': #mov register
            registerFile[reg1] = registerFile[reg2]
            registerFile['111'] = '0000000000000000'
        elif opcode == '01110':  #cmp
            if registerFile[reg1] < registerFile[reg2]:
                registerFile['111'] = '0000000000000100'
            elif registerFile[reg1] > registerFile[reg2]:
                registerFile['111'] = '0000000000000010'
            elif registerFile[reg1] == registerFile[reg2]:
                registerFile['111'] = '0000000000000001'
        elif opcode == '01101': #not
            temp = ''
            for i in registerFile[reg2]:
                if i == '1':
                    temp += '0'
                else:
                    temp += '1'
            registerFile[reg1] = temp
        elif opcode == '00111':
            q = int(registerFile[reg1], 2) // int(registerFile[reg2], 2)
            r = int(registerFile[reg1], 2) % int(registerFile[reg2], 2)
            registerFile['000'] = convertToBin(q, 16)
            registerFile['001'] = convertToBin(r, 16)
            
    elif type == 'D':
        reg = instruction[5:8]
        addr = instruction[8:16]
        if opcode == '00100': #ld
            registerFile[reg] = memory[int(addr, 2)]
        elif opcode == '00101': #ld
            memory[int(addr, 2)] = registerFile[reg]
        registerFile['111'] = '0000000000000000'
    elif type == 'E':
        addr = instruction[8:16]
        if opcode == '01111':
            programCounter = int(addr, 2) - 1 #jmp
        elif opcode == '10000' and registerFile['111'] == '0000000000000100':
            programCounter = int(addr, 2) - 1 #jlt
        elif opcode == '10001' and registerFile['111'] == '0000000000000010':
            programCounter = int(addr, 2) - 1 #jgt
        elif opcode == '10010' and registerFile['111'] == '0000000000000001':
            programCounter = int(addr, 2) - 1 #jgt
        registerFile['111'] = '0000000000000000'
    elif type == 'F':
        return True
    return False

def convertToBin(num, bits):
    temp = ''
    num = format(num, 'b')
    while len(temp) < bits - len(num):
        temp += '0'
    return temp + num

def main():
    while True:
        try:
            line = input()
            memory.append(line)
        except EOFError:
            break
    while len(memory) < 256:
        memory.append('0000000000000000')
    global programCounter
    halted = False
    while not halted:
        halted = executionEngine(memory[programCounter])
        print(convertToBin(programCounter, 8), end= " ")
        for key in registerFile:
            print(registerFile[key], end = " ")
        print()
        programCounter += 1
    for mem in memory:
        print(mem)  # add

if __name__ == '__main__':
    main()