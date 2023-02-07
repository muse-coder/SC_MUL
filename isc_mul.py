import random
from sobolsampling.sobol_new import sobol_points
import  math

def stream_gen(operator,sobol_sequence):
    length = len(sobol_sequence)
    bit_stream = []
    # # print(to_bin(operator,16))
    for i in range(length):
        # # print(to_bin(sobol_sequence[i],16))
        if operator > sobol_sequence[i]:
            bit_stream.append(1)
        else:
            bit_stream.append(0)
    return bit_stream        

def calculate(sequence_1,sequence_2):
    length = len(sequence_1)
    APC=0
    for i in range(length):
        APC  += sequence_1[i] & sequence_2[i]
    
    # print("APC=%d"%APC)
    return APC

def ISC_MUL(num_1,num_2,sobol_1,sobol_2,bit):
    num_1_shift = leading_zero_shift(num_1,bit)
    num_2_shift = leading_zero_shift(num_2,bit)
    scaled_num_1 = num_1 << num_1_shift
    scaled_num_2 = num_2 << num_2_shift
    # print("scaled_num_1:",to_bin(scaled_num_1,bit))
    # print("scaled_num_2:",to_bin(scaled_num_2,bit))
    scaled_sobol_1 = [sobol_1[i]<<(bit-5) for i in range(len(sobol_1))]
    scaled_sobol_2 = [sobol_2[i]<<(bit-5) for i in range(len(sobol_2))] 
    # print("sobol_1")
    # for i in scaled_sobol_1:
        # print(to_bin(i,bit))
    
    # print("sobol_2")
        
    # for j in scaled_sobol_2:
        # print(to_bin(j,bit))

    bit_stream_1 = stream_gen(scaled_num_1,scaled_sobol_1)
    bit_stream_2 = stream_gen(scaled_num_2,scaled_sobol_2)
    # print("bit_stream_1:",bit_stream_1)
    # print("bit_stream_2:",bit_stream_2)
    scaled_res = calculate(bit_stream_1,bit_stream_2)
    
    res = scaled_res<<(2*bit-num_1_shift-num_2_shift-5)
    # print("scale=%d"%((2*bit-num_1_shift-num_2_shift-5)))
    return res

    
def MRED(bit):
    test_range=pow(2,bit)    
    for i in test_range:
        num_1=random.randint(1,test_range)
        num_2=random.randint(1,test_range)
        exact_res=num_1*num_2
        isc_res=ISC_MUL(num_1,num_2,sobol_1,sobol_2)


def to_bin(value, num):#十进制数据，二进制位宽
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串


def leading_zero_shift(value,bit):
    bin_str=to_bin(value,bit)
    # print(bin_str)
    length=len(bin_str)
    count=0
    for i in range(length):
        if bin_str[i]=='0':
           count+=1
           continue 
        else:
            break
    return count

def excute(num_1,num_2,sobol_1,sobol_2,bit):
    exact_res=num_1*num_2
    isc_res=ISC_MUL(num_1,num_2,sobol_1,sobol_2,16)
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    # print("ISC_MUL: %.2lf "%(error*100) + '%',end='')

    return error

if __name__=="__main__":
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    bit = 16
    # test_range=pow(2,bit)  
    test_range=1000  
    num_2=555
    num_1=777
    exact_res=num_1*num_2

    isc_res=ISC_MUL(num_1,num_2,sobol_1,sobol_2,bit)
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    print(error)
    sum=0
    # for i in range(test_range):
    #     num_1=random.randint(1,test_range)
    #     num_2=random.randint(1,test_range)
    #     exact_res=num_1*num_2
    #     isc_res=ISC_MUL(num_1,num_2,sobol_1,sobol_2,bit)
    #     ED = abs(exact_res-isc_res)
    #     error= ED/exact_res
    #     sum+=error
    #     # print(num_1 , num_2, error)
    # MRED=sum/test_range
    # # print("MRED = %.2lf"%(MRED*100)+"%")