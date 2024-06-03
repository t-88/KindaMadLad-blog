MEM = [0] * (0xFFF + 1)

i = 0
with open("rom","rb") as f:
    while True and i < 0x400:
        b = f.read(1)
        if not b: break
        MEM[0x100 + i    ] = int(b.hex(),16)
        MEM[0x100 + i + 1] = int(f.read(1).hex(),16)
        i += 2    

A = 0
PC = 0x100
blocked = [False] * (0xFFF + 1)

while True:
    v = False

    fop = MEM[PC] << 8 | MEM[PC + 1]
    op = MEM[PC]
    hop = (op & 0xF0) >> 4

    arg = MEM[PC + 1] 
    addr = fop & 0xFFF
    PC += 2


    
   
    # arth
    if op == 0x00: A += arg    # 00 XX Add XX to A and store the result in A
    elif op == 0x01: A = arg   # 01 XX Set A = XX
    elif op == 0x02: A ^= arg  # 02 XX Xor A with XX and store the result in A
    elif op == 0x03: A |= arg  # 03 XX Or A with XX and store the result in A
    elif op == 0x04: A &= arg  # 04 XX And A with XX and store the result in A
    elif hop == 0x08: A = MEM[addr]  # 8X XX Set A = [XXX]
    elif hop == 0x0D: # DX XX Xor [XXX] with A and store the result in [XXX]
        if not blocked[addr]: MEM[addr] ^= A   
    elif hop == 0x0F:  # FX XX Set [XXX] = A  
        if not blocked[addr]: MEM[addr] = A   

    # io
    elif fop == 0x1337: 
        print(chr(A),end="") #13 37 Send A to Serial Out
        if chr(A) == "}":
            exit()
    # control flow
    elif hop == 0x02: PC = addr # 2X XX Jump to Address XXX
    elif hop == 0x03: 
        if A == 0:  PC = addr  # 3X XX Jump to Address XXX if A = 0
    elif hop == 0x04: 
        if A == 1:  PC = addr  # 4X XX Jump to Address XXX if A = 1
    elif hop == 0x05: 
        if A == 255:  PC = addr  # 5X XX Jump to Address XXX if A = 255
    elif op == 0x60: # 60 XX Compare A to XX and store comparison result in A
        if A > arg: A = 255
        elif A == arg: A = 0
        else: A = 1
    elif hop == 0x07: # 7X XX Compare A to [XXX] and store comparison result in A
        if A > MEM[addr]: A = 255
        elif A == MEM[addr]: A = 0
        else: A = 1
    elif fop == 0xBEEF: # BE EF Jump to 0x100 and set A = 0x42
        PC = 0x100
        A = 0x42

    # security
    elif hop == 0x09: blocked[addr] = True # 9X XX Block Writes to [XXX]
    elif hop == 0x0A: blocked[addr] = False # AX XX Unblock Writes to [XXX]
    elif hop == 0x0C: # CX XX Frobnicate [XXX] and store the result in [XXX]    
        if not blocked[addr]: MEM[addr] ^= 0x42

    elif fop == 0xEEEE: pass # EE EE No Operation
    else:
        A -= 1

    A &= 0xFF


