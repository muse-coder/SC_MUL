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
    # print("sobol: " )
    # print(scaled_sobol_1)
    # for i in range(length):
    #     print(to_bin(scaled_sobol_sequence[i],validSegWidth))
    for i in range(length):
        # print(to_bin(scaled_sobol_sequence[i],validSegWidth))
        if operator > (sobol_sequence[i]<<(validSegWidth - sobolWidth)):
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

def scaled_mul(num_1,num_2,sobol_1,sobol_2,validSegWidth,sobolWidth,dataWidth=16):
    scaled_num_1 , num_1_shift = sliding_window(num_1,dataWidth= dataWidth  ,validSegWidth=validSegWidth)
    scaled_num_2 , num_2_shift = sliding_window(num_2,dataWidth= dataWidth  ,validSegWidth=validSegWidth)

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
    scaled_res = calculate(bit_stream_1,bit_stream_2)
    # res = scaled_res<<(dataWidth-sobolWidth-num_1_shift-num_2_shift)
    shiftSum = dataWidth-sobolWidth-num_1_shift-num_2_shift
    if(shiftSum >=0):
        res = scaled_res <<shiftSum
    else:
        res = scaled_res >>(-shiftSum)
    # if()
    # print("scale=%d"%(5-num_1_shift-num_2_shift))

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
        shift_count = -(dataWidth-count-validSegWidth)
    else:
        valid_segment=bin_str[count:length] 
        for i in range(validSegWidth-(length-count)):
            valid_segment = valid_segment + '0'
        shift_count = count+validSegWidth-dataWidth
    scaled_num=int(valid_segment, 2)
    
    return scaled_num,shift_count

def excute_scaled_mul(num_1,num_2,sobol_1,sobol_2,dataWidth):
    isc_res=scaled_mul(num_1,num_2,sobol_1,sobol_2,dataWidth)
    exact_res=num_1*num_2
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    # print("ISC_MUL_plus: %.2lf "%(error*100) + '%',end='')
    return error


if __name__=="__main__":
# 0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1,
# 0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17,
# 0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29,
# 0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31,
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    dataWidth = 16
    test_range=pow(2,16)    
    num_1=1
    num_2=2
    exact_res=num_1*num_2
    validSegWidth = 8
    sobolWidth = 5
    isc_res=scaled_mul(num_1,num_2,sobol_1,sobol_4,validSegWidth,sobolWidth,dataWidth=16)
    ED = abs(exact_res-isc_res)
    error= ED/exact_res
    print(error)
    print("error = %.2lf"%(error*100)+"%")

    group_1=[sobol_1,sobol_2]
    group_2=[sobol_1,sobol_3]
    group_3=[sobol_1,sobol_4]
    group_4=[sobol_2,sobol_3]
    group_5=[sobol_2,sobol_4]
    group_6=[sobol_3,sobol_4]
    
    GROUPS=[group_1,group_2,group_3,group_4,group_5,group_6]
    errorSum = 0
    mredGroup = []
    for i in range (len(GROUPS)):
        mredGroup.append(0)

    # errorSumGroup = []
    for data in range(test_range):
        num_1=random.randint(1,test_range)
        num_2=random.randint(1,test_range)
        exact_res=num_1*num_2
        print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
        averageError= 0
        for i in range(len(GROUPS)):
            isc_res=scaled_mul(
                num_1=num_1,num_2=num_2,
                sobol_1= GROUPS[i][0],sobol_2= GROUPS[i][1],validSegWidth= validSegWidth,
                sobolWidth= sobolWidth,dataWidth=  16
            )
            ED = abs(exact_res-isc_res)
            error= ED/exact_res
            mredGroup[i] +=error
        # print(error)
            print("%.4lf"%(error*100)+"%",end= ' ;')
            averageError+=error
        averageError = averageError /len(GROUPS)  
        print("average Error: %.4lf"%(averageError*100)+"%")
        errorSum += averageError 
    mredGroup = [mredGroup [i] /test_range for i in range(len(mredGroup))]
    # scaled_sobol_sequence = [sobol_sequence[i]<<(validSegWidth - sobolWidth) for i in range(len(sobol_sequence))]

    MRED=errorSum/test_range
    print("average MRED = %.4lf"%(MRED*100)+"%")
    for i in range(len(mredGroup)):
        
        print("MRED %d = %.4lf"%(i+1,mredGroup[i]*100)+"% ",end=' ')
    averageMRED = statistics.mean(mredGroup)
    print("average MRED = %.4lf"%(MRED*100)+"%")
    
    # for g in GROUPS:
    #     isc_res=scaled_mul(
    #         num_1=num_1,num_2=num_2,
    #         sobol_1= g[0],
    #         sobol_2= g[1],
    #         validSegWidth= validSegWidth,
    #         sobolWidth= sobolWidth,
    #         dataWidth=  16
    #         )
        
    #     ED = abs(exact_res-isc_res)
    #     error= ED/exact_res
    #     # print(error)
    #     print("error = %.2lf"%(error*100)+"%",end= ' ;')

    # average_res = res/len(GROUPS)
    # print("average = ",average_res,end=' ')
    # print("average error rate = %lf "%((average_res-accurate_res)/accurate_res))
    # for i in range(test_range):
    #     num_1=random.randint(1,test_range)
    #     num_2=random.randint(1,test_range)
    #     exact_res=num_1*num_2
    #     isc_res=scaled_mul(num_1,num_2,sobol_1,sobol_2,dataWidth)
    #     ED = abs(exact_res-isc_res)
    #     error= ED/exact_res
    #     sum+=error
    #     # print(num_1,num_2,error)
    # MRED=sum/test_range
    # # print("MRED = %.2lf"%(MRED*100)+"%")