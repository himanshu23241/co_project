# converting immediate number to its corresponding binary number if it lies in range else return error
def imm_convert(imm,bits):
    if(imm>=-(2**(bits-1)) and imm<=((2**(bits-1))-1)):
        if(imm>=0):
            ans=(bin(imm)[2:])
            ans="0"*(bits-len(str(ans)))+str(ans)
            return ans
        else:
            ans=(bin(imm)[3:])
            ans="0"*(bits-len(str(ans)))+str(ans)
            # finding 2's complement
            s1=""
            for i in ans:
                if i=="0":
                    s1=s1+"1"
                else:
                    s1=s1+"0"
            ans=str(bin(int(s1,2)+1))[2:]
            return ans
    else:
        return "Error"

  # checking if instruction is b type
    if(instruction[0] in ins_b_opcode):
        # checking if there is label in instruction
        if(not(instruction[3].isalpha())):
            pass
        else:
            initial_position=get_line_initial(instruction[3])
            final_position=get_line_final(instruction[3]+":")
            instruction[3]=(initial_position-final_position)*4       
        immediate_value=imm_convert(int(instruction[3]),12)
        # check for errors
        if(immediate_value=="Error"):
            result += f"Error : illegal immediate in line {c}"
        elif(instruction[2] not in reg_dic or instruction[1] not in reg_dic):
            result += f"Syntax Error in line {c}"
        else:
            immediate_value=imm_convert(int(instruction[3]),32)
            result += immediate_value[19]+immediate_value[21:27]
            result += reg_dic[instruction[2]]
            result += reg_dic[instruction[1]]
            result += ins_b_opcode_funct3[instruction[0]]
            result += immediate_value[27:31]+immediate_value[20]
            result += ins_b_opcode[instruction[0]]
