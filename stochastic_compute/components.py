# import random
# from sobolsampling.sobol_new import sobol_points
# import  math

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

def isc_mul(num_1,num_2,sobol_1,sobol_2,bit_length,sobol_size):
    num_1_shift = leading_zero_shift(num_1,bit_length)
    num_2_shift = leading_zero_shift(num_2,bit_length)
    scaled_num_1 = num_1 << num_1_shift
    scaled_num_2 = num_2 << num_2_shift
    print("origin_num_1:",to_bin(num_1,bit_length))
    print("origin_num_2:",to_bin(num_2,bit_length))
    
    print("scaled_num_1:",to_bin(scaled_num_1,bit_length))
    print("scaled_num_2:",to_bin(scaled_num_2,bit_length))
    scaled_sobol_1 = [sobol_1[i]<<(16-sobol_size) for i in range(len(sobol_1))]
    scaled_sobol_2 = [sobol_2[i]<<(16-sobol_size) for i in range(len(sobol_2))] 
    # print("sobol_1")
    # for i in scaled_sobol_1:
        # print(to_bin(i,bit_length))
    
    # print("sobol_2")
        
    # for j in scaled_sobol_2:
        # print(to_bin(j,bit_length))

    bit_stream_1 = stream_gen(scaled_num_1,scaled_sobol_1)
    bit_stream_2 = stream_gen(scaled_num_2,scaled_sobol_2)
    print("bit_stream_1:",bit_stream_1)
    print("bit_stream_2:",bit_stream_2)
    scaled_res = calculate(bit_stream_1,bit_stream_2)
    
    if(2*bit_length-num_1_shift-num_2_shift-5>0):
        res = scaled_res<<(2*bit_length-num_1_shift-num_2_shift-5)
    else:
        res = scaled_res>>(-(2*bit_length-num_1_shift-num_2_shift-5))
        
    # print("scale=%d"%((2*bit_length-num_1_shift-num_2_shift-5)))
    return res

def sliding_window(value,bitWidth,segWidth):
    bin_str=to_bin(value,bitWidth)
    # # print(bin_str)
    length=len(bin_str)
    shift_count=0
    count=0
    for i in range(length):
        if bin_str[i]=='0':
           count+=1
           continue 
        else:
            break
    valid_segment=[]
    if(count<length-segWidth):
        valid_segment=bin_str[count:count + segWidth]
        shift_count = -(bitWidth-count-segWidth)
    else:
        valid_segment=bin_str[count:length] 
        for i in range(segWidth-(length-count)):
            valid_segment = valid_segment + '0'
        shift_count = count+segWidth-bitWidth
    scaled_num=int(valid_segment, 2)
    
    return scaled_num,shift_count



def to_bin(value, num):#十进制数据，二进制位宽
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串


def leading_zero_shift(value,bit_length):
    bin_str=to_bin(value,bit_length)
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

def scaled_mul(num_1,num_2,sobol_1,sobol_2,bitWidth,sobolWidth):
    scaled_num_1 , num_1_shift = sliding_window(num_1,bitWidth,sobolWidth)
    scaled_num_2 , num_2_shift = sliding_window(num_2,bitWidth,sobolWidth)

    # print("scaled_num_1:",to_bin(scaled_num_1,bitWidth))
    # print("scaled_num_2:",to_bin(scaled_num_2,bitWidth))

    # print("sobol_1")
    # for i in sobol_1:
        # print(to_bin(i,bitWidth))
    
    # print("sobol_2")
        
    # for j in sobol_2:
        # print(to_bin(j,bitWidth))


    bit_stream_1 = stream_gen(scaled_num_1,sobol_1)
    bit_stream_2 = stream_gen(scaled_num_2,sobol_2)
    # print("bit_stream_1:",bit_stream_1)
    # print("bit_stream_2:",bit_stream_2)

    scaled_res = calculate(bit_stream_1,bit_stream_2)
    res = scaled_res<<(5-num_1_shift-num_2_shift)
    # print("scale=%d"%(5-num_1_shift-num_2_shift))

    return res


def excute_isc_mul(num_1,num_2,sobol_1,sobol_2,bit_length,sobol_size):
    exact_res=num_1*num_2
    isc_res=isc_mul(num_1,num_2,sobol_1,sobol_2,bit_length,sobol_size)
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    # print("isc_mul: %.2lf "%(error*100) + '%',end='')
    return error

def excute_scaled_mul(num_1,num_2,sobol_1,sobol_2,bit_length,sobol_size):
    isc_res=scaled_mul(num_1,num_2,sobol_1,sobol_2,bit_length)
    exact_res=num_1*num_2
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    # print("ISC_MUL_plus: %.2lf "%(error*100) + '%',end='')
    return error