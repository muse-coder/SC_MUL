import random
# from statistics import mean 
import math
import statistics


def stream_gen(operator,sobol_sequence ,validSegWidth,sobolWidth):
    length = len(sobol_sequence)
    bit_stream = []
    operatorBinary=(to_bin(operator,validSegWidth))
    # print("operator:" + operatorBinary)
    scaled_sobol_sequence = [sobol_sequence[i]<<(validSegWidth - sobolWidth) for i in range(len(sobol_sequence))]
    # for i in range(length):
    #     print(to_bin(scaled_sobol_sequence[i],validSegWidth))

    for i in range(length):
        if operator > (scaled_sobol_sequence[i]):
            bit_stream.append(1)
        else:
            bit_stream.append(0)
    
    return bit_stream        
def	fullAdder(a , b ,cin):
	cout = (a&b) | (b&cin) | (cin&a)
	sum = a ^ b ^ cin 
	return sum ,cout

def	halfAdder(a,b):
	cout = (a&b)
	sum = a ^ b
	return sum, cout
def approximate_APC_16(stream_16):
	mid=[]
	for i in range (16):
		mid.append(0)
	# mid = (mid.append(0) for i in range(16))
	assert (len(stream_16)==16)
	mid[0] = stream_16[0]	 |	stream_16[1] 
	mid[1] = stream_16[2]	 &	stream_16[3]
	mid[2] = stream_16[4]	 |	stream_16[5]
	mid[3] = stream_16[6]	 &	stream_16[7]
	mid[4] = stream_16[8]	 |	stream_16[9]
	mid[5] = stream_16[10]   &	stream_16[11]
	mid[6] = stream_16[12]   |	stream_16[13]
	mid[7] = stream_16[14]   &	stream_16[15]
	fa1_sum ,fa1_cout = fullAdder(a= mid[0],b= mid[1],cin= mid[2])
	fa2_sum ,fa2_cout = fullAdder(a= mid[3],b= mid[4],cin= mid[5])
	fa3_sum ,fa3_cout = fullAdder(a= fa1_sum,b= fa2_sum,cin= mid[6])
	fa4_sum ,fa4_cout = fullAdder(a= fa1_cout,b= fa2_cout,cin= fa3_cout)
	# sum_str = str(fa4_cout)+str(fa4_sum)+str(fa3_sum ^ mid[7])+ str(mid[7])
	sum_str = str(fa4_cout)+str(fa4_sum)+str(fa3_sum )+ str(stream_16[14]   |	stream_16[15])
	sum = int(sum_str, 2)
	return sum

def approximate_APC_32(stream_32):
	mid=[]
	for i in range (16):
		mid.append(0)
	# mid = (mid.append(0) for i in range(16))
	assert (len(stream_32)==32)
	mid[0] = stream_32[0]	 |	stream_32[1] 
	mid[1] = stream_32[2]	 &	stream_32[3]
	mid[2] = stream_32[4]	 |	stream_32[5]
	mid[3] = stream_32[6]	 &	stream_32[7]
	mid[4] = stream_32[8]	 |	stream_32[9]
	mid[5] = stream_32[10]   &	stream_32[11]

	mid[6] = stream_32[20]   |	stream_32[21]
	mid[7] = stream_32[22]   &	stream_32[23]
	mid[8] = stream_32[24]	 |	stream_32[25]
	mid[9] = stream_32[26]	 &	stream_32[27]
	mid[10] = stream_32[28]	 |	stream_32[29]
	mid[11] = stream_32[30]   &	stream_32[31]
	


	fa_1_1_sum ,fa_1_1_cout = fullAdder(a= mid[0],b= mid[1],cin= mid[2])
	fa_1_2_sum ,fa_1_2_cout = fullAdder(a= mid[3],b= mid[4],cin= mid[5])
	fa_1_3_sum ,fa_1_3_cout = fullAdder(a= mid[6],b= mid[7],cin= mid[8])
	fa_1_4_sum ,fa_1_4_cout = fullAdder(a= mid[9],b= mid[10],cin= mid[11])
	fa_1_5_sum ,fa_1_5_cout = fullAdder(a= stream_32[12],b= stream_32[13],cin= stream_32[14])
	fa_1_6_sum ,fa_1_6_cout = fullAdder(a= stream_32[15],b= stream_32[16],cin= stream_32[17])
	# fa_1_7_sum ,fa_1_7_cout = halfAdder(a= stream_32[18],b= stream_32[19])
	
	fa_2_4_sum ,fa_2_4_cout = fullAdder(a= fa_1_3_sum,b= fa_1_4_sum ,cin= fa_1_5_cout)
	fa_2_3_sum ,fa_2_3_cout = fullAdder(a= fa_1_3_cout,b= fa_1_4_cout,cin= fa_2_4_cout)
	fa_2_2_sum ,fa_2_2_cout = fullAdder(a= fa_1_1_sum,b= fa_1_2_sum ,cin= fa_1_6_cout)
	fa_2_1_sum ,fa_2_1_cout = fullAdder(a= fa_1_1_cout,b= fa_1_2_cout , cin= fa_2_2_cout)
	# temp_sum ,temp_cout = halfAdder(a= stream_32[16],b= stream_32[17])
	fa_3_3_sum ,fa_3_3_cout = fullAdder(a= fa_2_2_sum,b= fa_2_4_sum,cin= stream_32[18]|stream_32[19])
	fa_3_2_sum ,fa_3_2_cout = fullAdder(a= fa_2_1_sum,b= fa_2_3_sum,cin= fa_3_3_cout)
	fa_3_1_sum ,fa_3_1_cout = fullAdder(a= fa_2_1_cout,b= fa_2_3_cout,cin= fa_3_2_cout)
	# fa_4_1_sum ,fa_4_1_cout = halfAdder(a=fa_3_2_sum ,b= fa_1_5_cout)

	sum_str = str(fa_3_1_cout)+str((fa_3_1_sum ))+str(fa_3_2_sum )+ str(fa_3_3_sum)+str(fa_1_5_sum|fa_1_6_sum)
	sum = int(sum_str, 2)
	# sum = sum + (fa_3_2_sum <<2)
	return sum



def accurate_APC(stream):
	# assert (len(stream_16)==16 or len(stream_16)==32)
	count = 0
	for i in range(len(stream)):
		count += stream[i]
	
	return count

def SN_To_BN(sequence_1,sequence_2):
	length = len(sequence_1)
	assert ((length == 32) or (length == 64))
	stream = []

	for i in range(length):
		stream.append(sequence_1[i] & sequence_2[i]) 
	
	accurate_sum = accurate_APC(stream=stream)
	# print(sequence_1)
	# print(sequence_2)
	# print(stream_32)
	if(length ==32):
		stream_16_left = stream[0:16]
		stream_16_left_reverse = list(reversed(stream_16_left))
		stream_16_right = stream[16:32]
		stream_16_right_reverse = list(reversed(stream_16_right))
		approximate_sum_1 = approximate_APC_16(stream_16=stream_16_left)
		approximate_sum_1_revese = approximate_APC_16(stream_16= stream_16_left_reverse)
		approximate_sum_2 = approximate_APC_16(stream_16=stream_16_right)
		approximate_sum_2_revese = approximate_APC_16(stream_16= stream_16_right_reverse)

		accurate_sum_1 = accurate_APC(stream= stream_16_left)
		accurate_sum_2 = accurate_APC(stream= stream_16_right)
		sum = approximate_sum_1 +approximate_sum_2_revese
	if(length ==64):
		approximate_sum_1 = approximate_APC_16(stream_16=stream[0:16])
		# approximate_sum_1_revese = approximate_APC_16(stream_16= stream_16_left_reverse)
		approximate_sum_2 = approximate_APC_16(stream_16=list(reversed(list(stream[16:32]))))
		approximate_sum_3 = approximate_APC_16(stream_16=stream[32:48])
		approximate_sum_4 = approximate_APC_16(stream_16=list(reversed(list(stream[48:64]))))
		sum = approximate_sum_1 + approximate_sum_2 +approximate_sum_3 +approximate_sum_4
# print("approximate_sum_1:%d"%(approximate_sum_1))
	# print("approximate_sum_1_reverse:%d"%(approximate_sum_1_revese))

	# print("approximate_sum_2:%d"%(approximate_sum_2))
	# print("approximate_sum_2_reverse:%d"%(approximate_sum_2_revese))

	# print("accurate_sum_1:%d"%(accurate_sum_1))
	# print("accurate_sum_2:%d"%(accurate_sum_2))
	# sum =approximate_APC_32(stream_32=stream_32)

	return sum
	# return accurate_sum
	# return int((approximate_sum_1+approximate_sum_1_revese)/2) + int((approximate_sum_2+approximate_sum_2_revese)/2)
	# return accurate_sum_1+accurate_sum_2
	


def scaled_mul(num_1,num_2,sobol_1,sobol_2,validSegWidth,sobolWidth,dataWidth=16):
    scaled_num_1 , num_1_shift = sliding_window(num_1,dataWidth= dataWidth  ,validSegWidth=validSegWidth)
    scaled_num_2 , num_2_shift = sliding_window(num_2,dataWidth= dataWidth  ,validSegWidth=validSegWidth)
    # print("validSegWidth =%d"%validSegWidth)
    # print("scaled_num_1:",to_bin(scaled_num_1,dataWidth))
    # print("scaled_num_2:",to_bin(scaled_num_2,dataWidth))

    # print("sobol_1")
    # for i in sobol_1:
        # print(to_bin(i,dataWidth))
    
    # print("sobol_2")
        
    # for j in sobol_2:
        # print(to_bin(j,dataWidth))


    bit_stream_1 = stream_gen(operator=  scaled_num_1,sobol_sequence=  sobol_1,validSegWidth= validSegWidth, sobolWidth= sobolWidth)
    bit_stream_2 = stream_gen(operator=  scaled_num_2,sobol_sequence=  sobol_2,validSegWidth= validSegWidth, sobolWidth= sobolWidth)
    # print("bit_stream_1:",bit_stream_1)
    # print("bit_stream_2:",bit_stream_2)
    scaled_res = SN_To_BN(bit_stream_1,bit_stream_2)
    shiftSum = 2*dataWidth-sobolWidth-num_1_shift-num_2_shift
    exact_res = num_1 * num_2
    if(shiftSum >=0):
        res = scaled_res <<shiftSum
    else:
        res = scaled_res >>(-shiftSum)
    # print(res)
    ED = abs(exact_res-res)
    error= ED/exact_res
    # print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
    # print("%.4lf"%(error*100)+"%")
    return res

    

def to_bin(value, num):#十进制数据，二进制位宽
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串


def sliding_window(value,dataWidth,validSegWidth):
    bin_str=to_bin(value,dataWidth)
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
    if(count<length-validSegWidth):
        valid_segment=bin_str[count:count + validSegWidth]
        # shift_count = -(dataWidth-count-validSegWidth)
    else:
        valid_segment=bin_str[count:length] 
        for i in range(validSegWidth-(length-count)):
            valid_segment = valid_segment + '0'
        # shift_count = count+validSegWidth-dataWidth
    shift_count = count
    scaled_num=int(valid_segment, 2)
    
    return scaled_num,shift_count


