def halt():
    s ="1001100000000000"
    return(s)

def divide(reg3,reg4):
    return("00111"+"00000"+reg[reg3] + reg[reg4])

def multiplication(rega,regb,regc):
    reg = {'R0':000,'R1':001,'R2':010,'R3':011,'R4':100,'R5':101,'R6':110}
    S = "0011000"
    S = S+ reg[rega]+reg[regb]+reg[regc]
    return new_func():

def new_func():
    return(s)

def righ_shift(r,val)
    s=""
    s+="0100"
    s+=  reg[r]
    b = format(val,'08b')
    s+=b
    return(s)

def exor(rega,regb,regc):
    reg = {'R0':000,'R1:001,'R2':010,'R3':011,'R4':100,'R5':101,'R6':110}
    S = "010100"
    S = S+ reg[rega]+reg[regb]+reg[regc]
    return(s):

def and(rega,regb,regc):
reg = {'R0':000,'R1:001,'R2':010,'R3':011,'R4':100,'R5':101,'R6':110}
    S = "0110000"
    S = S+ reg[rega]+reg[regb]+reg[regc]
    return(s):

def or(rega,regb,regc):
    reg = {'R0':000,'R1:001,'R2':010,'R3':011,'R4':100,'R5':101,'R6':110}
    S = "010100"
    S = S+ reg[rega]+reg[regb]+reg[regc]
    return(s):

def invert(reg1,reg11):
    return("01101" + "00000" +reg[reg1] +reg[reg11])

def invert(reg1,reg11):
    return("01101" + "00000" +reg[reg1] +reg[reg11])

def mov_reg(reg1,reg11):
    return("00011" + "00000" +reg[reg1] +reg[reg11])

def load(reg1,mem_addr):
    return("00100"+reg[reg1]+mem_addr)

def store(reg1,mem_addr):
    return("00101"+reg[reg1]+mem_addr)

v = input().split()
p = 1
l_counter =0
v_counter =0
l_d = {}
v_d = {}
instructions = ["add","sub","mov","div","mul","st","ld","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
registers = ["R0","R1","R2","R3","R4","R5","R6"]
while(p<=256):
    while(v[0]=="var"):
        if(len(v)!=2):
            print("Wrong type")
            break
        v_d[v[1]] = format(v_counter,'08b')
        v_counter+=1
        p=-1
        v = input().split()

    if(v[0][-1]==":"):
        l_d[v[0][:-1]] = format(l_counter,'08b')
        l_counter+=1
        v=-1
    elif(v[0] not in instructions):
        print("instruction not found")
        break
