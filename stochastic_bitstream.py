# import math
def stream_gen(operator,sobol_sequence):
    length = len(sobol_sequence)
    bit_stream = []
    for i in range(length):
        if operator > sobol_sequence[i]:
            bit_stream.append(1)
        else:
            bit_stream.append(0)
    return bit_stream        
    
def get_result(sequence_1,sequence_2):
    length = len(sequence_1)
    APC=0
    for i in range(length):
        APC  += sequence_1[i] & sequence_2[i]
    return APC
    
if __name__ == '__main__':
    sobol_seq_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_seq_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_seq_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_seq_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    
    # sobol_64_seq_1=[0,32,48,16,24,56,40,8,12,44,60,28,20,52,36,4,6,38,54,22,30,62,46,14,10,42,58,26,18,50,34,2,3,35,51,19,27,59,43,11,15,47,63,31,23,55,39,7,5,37,53,21,29,61,45,13,9,41,57,25,17,49,33,1]
    # sobol_64_seq_2=[0,32,48,16,24,56,40,8,36,4,20,52,60,28,12,44,18,50,34,2,10,42,58,26,54,22,6,38,46,14,30,62,9,41,57,25,17,49,33,1,45,13,29,61,53,21,5,37,27,59,43,11,3,35,51,19,63,31,15,47,39,7,23,55]
    # sobol_64_seq_3=[0,32,48,16,40,8,24,56,20,52,36,4,60,28,12,44,10,42,58,26,34,2,18,50,30,62,46,14,54,22,6,38,3,35,51,19,43,11,27,59,23,55,39,7,63,31,15,47,9,41,57,25,33,1,17,49,29,61,45,13,53,21,5,37]
    # sobol_64_seq_4=[0,32,16,48,40,8,56,24,60,28,44,12,20,52,4,36,42,10,58,26,2,34,18,50,22,54,6,38,62,30,46,14,63,31,47,15,23,55,7,39,3,35,19,51,43,11,59,27,21,53,5,37,61,29,45,13,41,9,57,25,1,33,17,49]
    group_1=[sobol_seq_1,sobol_seq_2]
    group_2=[sobol_seq_1,sobol_seq_3]
    group_3=[sobol_seq_1,sobol_seq_4]
    group_4=[sobol_seq_2,sobol_seq_3]
    group_5=[sobol_seq_2,sobol_seq_4]
    group_6=[sobol_seq_3,sobol_seq_4]
    
    GROUPS=[group_1,group_2,group_3,group_4,group_5,group_6]
    # GROUPS=[group_1,group_2,group_3,group_4]
    # GROUPS=[group_1,group_1,group_1,group_1]
    
    x=19
    y=26
    accurate_res=x*y
    print("accurate result = %d"%accurate_res)
    res=0
    for g in GROUPS:
        x_sequence=stream_gen(x,g[0])
        # print(x_sequence)
        y_sequence=stream_gen(y,g[1])
        # print(y_sequence)
        result=get_result(x_sequence,y_sequence)<<(5)
        print("SC result = %d"%result,end=' ')
        print("error rate = %lf \n"%((accurate_res-result)/accurate_res))
        res+=result
    average_res = res/len(GROUPS)
    print("average = ",average_res,end=' ')
    print("average error rate = %lf "%((average_res-accurate_res)/accurate_res))
