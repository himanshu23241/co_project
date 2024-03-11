# function for spliting instruction
def split_ins(s1):
    # checking if it's a label type
    for i in s1:
        if i==":":
            l1=s1.split(" ")
            l2=l1[2].split(",")
            return [l1[1]]+l2
    l1=s1.split(" ")
    l2=l1[1].split(",")
    l1.pop()
    return l1+l2

    # checking if instruction is i type
    if(instruction[0] in ins_i_opcode):
        # check if instruction is lw
        if(instruction[0]=="lw"):
            l1=instruction[2].split("(")
            instruction[2]=l1[1][:-1]
            instruction.append(l1[0])
        immediate_value=imm_convert(int(instruction[3]),32)[20:]
        # check for errors
        if(immediate_value=="Error"):
            result += f"Error : illegal immediate in line {c}"
        elif(instruction[2] not in reg_dic or instruction[1] not in reg_dic):
            result += f"Syntax Error in line {c}"
        else:
            result += immediate_value
            result += reg_dic[instruction[2]]
            result += ins_i_opcode_funct3[instruction[0]]
            result += reg_dic[instruction[1]]
            result += ins_i_opcode[instruction[0]]

    # checking if instruction is s type
    if(instruction[0] in ins_s_opcode):
        # check if instruction is sw
        if(instruction[0]=="sw"):
            l1=instruction[2].split("(")
            instruction[2]=l1[1][:-1]
            instruction.append(l1[0])
        immediate_value=imm_convert(int(instruction[3]),32)
        # check for errors
        if(immediate_value=="Error"):
            result += f"Error : illegal immediate in line {c}"
        elif(instruction[2] not in reg_dic or instruction[1] not in reg_dic):
            result += f"Syntax Error in line {c}"
        else:
            result += immediate_value[20:27]
            result += reg_dic[instruction[1]]
            result += reg_dic[instruction[2]]
            result += ins_s_opcode_funct3[instruction[0]]
            result += immediate_value[27:]
            result += ins_s_opcode[instruction[0]]
