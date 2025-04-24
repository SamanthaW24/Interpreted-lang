import sys

lines = []
try:
    fileName = sys.argv[1]
    file = open(fileName)
    lines = file.read().split("\n")
    file.close()
except Exception as e:
    print(f"Error while opening file:\n{e}")
    sys.exit(0)

stack = []
pc = 0

def err(str):
    print("\n" + str + f" at line {pc}")
    sys.exit(0)

def pop(index=-1):
    if len(stack) < 1:
        err("Error: Stack underflow")
    return stack.pop(index)

while pc >= 0 and pc < len(lines):
    parts = lines[pc].split(" ")
    instr = parts[0]

    if instr == "NOX":
        stack.append(0)
    elif instr == "LUMOS":
        a = pop()
        stack.append(a + 1)
    elif instr == "REDUCTO":
        a = pop()
        stack.append(a-1)
    elif instr == "CONFRINGO":
        a = pop()
        if(a != 0):
            stack.append(a)
    elif instr == "ACCIO":
        a = pop()
        stack.append(a)
        stack.append(a)
    elif instr == "OBLIVIATE":
        try:
            stack.append(ord(input("")[0]))   
        except IndexError:
            stack.append(0)
    elif instr == "GEMINIO":
        a = pop()  
        b = pop()  
        result = a * b 
        stack.append(result)
    elif instr == "ENNERVATE":
        print(chr(pop()), end="", flush=True)
    elif instr == "STUPEFY":
        print(int(pop()), end="", flush=True)
    elif instr == "RIDDIKULUS":
        a = pop()  # Pop the top value, which is the counter
        stack.append(a)
        try:
            line = int(parts[1]) - 1  # Convert to 0-based index
            if a == 0:
                pc = line - 1  # Jump to the specified line if counter is 0
        except:
            err("Error: Invalid instruction argument for RIDDIKULUS")
    elif instr == "EXPELLIARMUS":
        a = pop()
        stack.insert(0, a)
    elif instr == "WINGARDIUM":
        if len(parts) < 2:
            err("Error: Expected to WINGARDIUM")
        if parts[1] == 'LEVIOSA':
            a = pop(0)
            stack.append(a)
    elif instr == "AVADA":
        if len(parts) < 2:
            err("Error: Expected to specify AVADA")
        if parts[1] == 'KEDAVRA':
            break
    elif instr == "LEGILIMENS":
        try:
            num = int(input().strip())
        except:
            num = 0
        stack.append(num)


    pc += 1

print('')
