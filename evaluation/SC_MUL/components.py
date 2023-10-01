import random
# from statistics import mean 
import math
import statistics


def stream_gen(operator,sobol_sequence ,validSegWidth,sobolWidth):
    length = len(sobol_sequence)
    bit_stream = []
    operatorBinary=(to_bin(operator,validSegWidth))
    # print("operator:" + operatorBinary)
    if (validSegWidth - sobolWidth >0):        
        scaled_sobol_sequence = [sobol_sequence[i]<<(validSegWidth - sobolWidth) for i in range(len(sobol_sequence))]
    
    else:
        scaled_sobol_sequence = [sobol_sequence[i]>>abs(validSegWidth - sobolWidth) for i in range(len(sobol_sequence))]
    
    for i in range(length):
        if operator > (scaled_sobol_sequence[i]):
            bit_stream.append(1)
        else:
            bit_stream.append(0)
    
    return bit_stream        

def calculate(sequence_1,sequence_2):
    length = len(sequence_1)
    APC=0
    for i in range(length):
        APC  += sequence_1[i] & sequence_2[i]
    # print("APC=%d "%APC,end=' ')
    return APC

def GenerateScaledSeq(length,dataWidth):
    Seq=[]
    for i in range(0,length):
        # k =int(i*pow(2,length)/length)
        Seq.append(i)
    return Seq

    

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

    sobol_2 = GenerateScaledSeq(len(sobol_1),dataWidth)
    bit_stream_1 = stream_gen(operator=  scaled_num_1,sobol_sequence=  sobol_1,validSegWidth= validSegWidth, sobolWidth= sobolWidth)
    bit_stream_2 = stream_gen(operator=  scaled_num_2,sobol_sequence=  sobol_2,validSegWidth= validSegWidth, sobolWidth= sobolWidth)
    # print("bit_stream_1:",bit_stream_1)
    # print("bit_stream_2:",bit_stream_2)
    scaled_res = calculate(bit_stream_1,bit_stream_2)
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

def RepresentationError(num_1,Sobol_1,validSegWidth,sobolWidth,dataWidth=16):
    scaled_num_1 , num_1_shift = sliding_window(num_1,dataWidth= dataWidth  ,validSegWidth=validSegWidth)
    bit_stream_1 = stream_gen(operator=  scaled_num_1,sobol_sequence=Sobol_1,validSegWidth= validSegWidth, sobolWidth= sobolWidth)
    length = len(bit_stream_1)
    APC=0
    for i in range(length):
        APC  += bit_stream_1[i]
    approx_num = APC << (dataWidth-sobolWidth)
    return approx_num

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

# def excute_scaled_mul(sobolGroups ,testRange , iterationRange , validSegWidthRange ,sobolWidth ,dataWidth ):
#     mredGroup = []
#     for i in range (len(sobolGroups)):
#         mredGroup.append([])
        
#     for test in range(iterationRange):
#         num_1=random.randint(testRange[0],testRange[1])
#         num_2=random.randint(testRange[0],testRange[1])
#         exact_res=num_1*num_2
#         print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
#         print("num1=%d,num2=%d,exact_res=%d"%(num_1,num_2,exact_res))
#         for i in range(len(sobolGroups)):
#             for segWidth in range(validSegWidthRange[0],validSegWidthRange[1]):
#                 isc_res=scaled_mul(
#                     num_1=num_1,num_2=num_2,
#                     sobol_1= sobolGroups[i][0],sobol_2= sobolGroups[i][1],validSegWidth=segWidth,
#                     sobolWidth= sobolWidth,dataWidth=  dataWidth
#                 )
#                 ED = abs(exact_res-isc_res)
#                 error= ED/exact_res
#                 mredGroup[i].append(error)
#         # print(error)
#             # print("isc_res=%d error %d= %.4lf"%(isc_res,i+1,error*100)+"%",end= ' ;')
#             # averageError+=error
#         # averageError = averageError /len(sobolGroups)  
#         # print("\naverage Error: %.4lf"%(averageError*100)+"%")
#         # errorSum += averageError 
#     # MRED=errorSum/iterationRange
#     # print("average MRED = %.4lf"%(MRED*100)+"%")
    
#     mredGroup = [mredGroup [i] /iterationRange for i in range(len(mredGroup))]

#     for i in range(len(mredGroup)):
        
#         print("MRED %d = %.4lf"%(i+1,mredGroup[i]*100)+"% ",end=' ')
#     averageMRED = statistics.mean(mredGroup)
#     print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")

#     return mredGroup ,averageMRED

