# function to get line number
def get_line_initial(s1):
    file=open(file_name, "r")
    ins_num=file.readlines()
    count=0
    for line in ins_num:
        cleaned_line = line.lstrip()
        cleaned_line = cleaned_line.rstrip()
        if cleaned_line: #taking care of empty line 
            if((s1 in cleaned_line) and (s1+":" not in cleaned_line)):
                return count
            count=count+1
    file.close()        


# function to get line number
def get_line_final(s1):
    file=open(file_name, "r")
    ins_num=file.readlines()
    count=0
    for line in ins_num:
        cleaned_line = line.lstrip()
        cleaned_line = cleaned_line.rstrip()
        if cleaned_line: #taking care of empty line 
            if((s1 in cleaned_line)):
                return count
            count=count+1
    file.close() 

    # checking if instruction is r type
    if(instruction[0] in ins_r_opcode):
        # check for errors
        if(instruction[1] not in reg_dic or instruction[2] not in reg_dic or instruction[3] not in reg_dic):
            result += f"Syntax Error in line {c}"
        else:
            result += ins_r_opcode_funct7[instruction[0]]
            result += reg_dic[instruction[3]]
            result += reg_dic[instruction[2]]
            result += ins_r_opcode_funct3[instruction[0]]
            result += reg_dic[instruction[1]]
            result += ins_r_opcode[instruction[0]]
