# checking if instruction is u type
    if(instruction[0] in ins_u_opcode):
        immediate_value=imm_convert(int(instruction[2]),32)[0:20]
        # check for errors
        if(immediate_value=="Error"):
            result += f"Error : illegal immediate at line {c}"
            
        elif(instruction[1] not in reg_dic):
            result += f"Syntax Error at line {c}"
        else:
            result += immediate_value
            result += reg_dic[instruction[1]]
            result += ins_u_opcode[instruction[0]]

    # checking if instruction is j type
    if(instruction[0] in ins_j_opcode):
        # checking if there is label in instruction
        if(not(instruction[2].isalpha())):
            pass
        else:
            initial_position=get_line_initial(instruction[2])
            final_position=get_line_final(instruction[2]+":")
            instruction[2]=(initial_position-final_position)*4 
        immediate_value=imm_convert(int(instruction[2]),32)
        # check for errors
        if(immediate_value=="Error"):
            result += f"Error : illegal immediate at line {c}"
        elif(instruction[1] not in reg_dic):
            result += f"Syntax Error at line {c}"
        else:
            result += immediate_value[11]+immediate_value[21:31]+immediate_value[20]+immediate_value[12:20]
            result += reg_dic[instruction[1]]
            result += ins_j_opcode[instruction[0]]

      ins_r_opcode={"add":"0110011","sub":"0110011","sll":"0110011","slt":"0110011"
              ,"sltu":"0110011","xor":"0110011","srl":"0110011","or":"0110011","and":"0110011"}
ins_r_opcode_funct3={"add":"000","sub":"000","sll":"001","slt":"010"
              ,"sltu":"011","xor":"100","srl":"101","or":"110","and":"111"}
ins_r_opcode_funct7={"add":"0000000","sub":"0100000","sll":"0000000","slt":"0000000"
              ,"sltu":"0000000","xor":"0000000","srl":"0000000","or":"0000000","and":"0000000"}
ins_i_opcode={"lw":"0000011","addi":"0010011","sltiu":"0010011","jalr":"1100111"}
ins_i_opcode_funct3={"lw":"010","addi":"000","sltiu":"011","jalr":"000"}
ins_s_opcode={"sw":"0100011"}
ins_s_opcode_funct3={"sw":"010"}
ins_b_opcode={"beq":"1100011","bne":"1100011","blt":"1100011"
              ,"bge":"1100011","bltu":"1100011","bgeu":"1100011"}
ins_b_opcode_funct3={"beq":"000","bne":"001","blt":"100","bge":"101","bltu":"110","bgeu":"111"}
ins_u_opcode={"lui":"0110111","auipc":"0010111"}
ins_j_opcode={"jal":"1101111"}


reg_dic={"zero":"00000","ra":"00001","sp":"00010","gp":"00011"
        ,"tp":"00100","t0":"00101","t1":"00110","t2":"00111"
        ,"s0":"01000","fp":"01000","s1":"01001","a0":"01010","a1":"01011"
        ,"a2":"01100","a3":"01101","a4":"01110","a5":"01111"
        ,"a6":"10000","a7":"10001","s2":"10010","s3":"10011"
        ,"s4":"10100","s5":"10101","s6":"10110","s7":"10111"
        ,"s8":"11000","s9":"11001","s10":"11010","s11":"11011"
        ,"t3":"11100","t4":"11101","t5":"11110","t6":"11111"
        }
