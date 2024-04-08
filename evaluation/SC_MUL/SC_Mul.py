import torch
import math
import time
def TensorGenBitstream(rngSeq,tensorInputData,index,dataWidth = 8 ):
    len = rngSeq.size(0)
    quantizedata = (torch.round(tensorInputData / (2 ** (dataWidth - math.log2(len))))).to(rngSeq.device)


    singleBitstream = (quantizedata> rngSeq[index]).int()
    return singleBitstream

def tensorGenBitstreamMulti(rngSeq,tensorInputData,dataWidth = 8  ):
    len = rngSeq.size(0)
    quantizeData = (torch.round(tensorInputData / (2 ** (dataWidth - math.log2(len))))).to(rngSeq.device)
    quantizeDataMul = quantizeData.unsqueeze(2)
    rngSeqMul = rngSeq.unsqueeze(0).unsqueeze(1)
    singleBitstreamMul = (quantizeDataMul> rngSeqMul).int()
    quantizeData_T = torch.transpose(input=quantizeData,dim0=0,dim1=1)
    singleBitstreamMul_T = torch.transpose(input=singleBitstreamMul,dim0=0,dim1=1)
    # originalQuantizeData = torch.sum(input = singleBitstreamMul,dim= 2 )


    return singleBitstreamMul


def tensorGenBitstreamSeries(rngSeq,tensorInputData,index,dataWidth = 8  ):
    length = len(rngSeq)
    quantizeData = (torch.round(tensorInputData / (2 ** (dataWidth - math.log2(length))))).to(tensorInputData.device)
    singleBitstreamMul = (quantizeData> rngSeq[index]).int()


    return singleBitstreamMul





def FindHighestOne(num, dataWidth):
    mask = 1 << (dataWidth - 1)  # 创建一个掩码，将其移到最高位
    data = int(num.item())
    for position in range(dataWidth - 1, -1, -1):
        if data & mask:
            return position
        mask >>= 1  # 右移掩码，检查下一位
    return None


def TensorFindHighestOne(tensor):
    # 将张量转换为整数类型（如果是浮点数）
    tensor = tensor.to(torch.int)

    # 获取张量中每个元素的二进制表示
    binary_strings = [format(int(num.item()), 'b') for num in tensor.reshape(-1)]

    # 计算每个二进制字符串的有效位数
    significant_bits = [len(binary_string) for binary_string in binary_strings]

    # 将有效位数还原为与输入张量相同的形状
    significant_bits_tensor = torch.tensor(significant_bits).view(tensor.shape)
    result = (significant_bits_tensor - 1).to(tensor.device)
    return result

def TensorLeftShiftBits(data,dataWidth):
    # 将张量转换为整数类型（如果是浮点数）
    # dataExceptZero = torch.where(data>0 , data, 2**dataWidth-1)
    dividedData = (2**dataWidth-1)/data
    log2Result =torch.log2(dividedData)
    log2ResultFloor = torch.floor(log2Result)
    return log2ResultFloor



def EnlargeModule(originalData, dataWidth):
    if originalData == 0:
        return 0,0
    # binary_str = format(originalData, f"0{dataWidth}b")
    leftShiftTime = dataWidth -  FindHighestOne(originalData,dataWidth) - 1
    enlargedNumber = int(originalData.item()) << leftShiftTime

    return enlargedNumber , leftShiftTime

def TensorEnlargeModule(tensorData, dataWidth):
    # leftShiftTimeTensor = dataWidth - TensorFindHighestOne(tensorData) - 1
    leftShiftTimeTensor = TensorLeftShiftBits(data= tensorData , dataWidth= dataWidth)
    enlargedNumberTensor = tensorData *(2**leftShiftTimeTensor)

    return enlargedNumberTensor.to(torch.int32) , leftShiftTimeTensor.to(torch.int32)

def BitstreamMUL(bitstream_1,bitstream_2,leftshit_1,leftshit_2,rngSeqLengthLog,dataWidth):
    resultBitstream = (bitstream_1.int() & bitstream_2.int())
    resultSum = resultBitstream.sum()
    resultBinary = (resultSum * (2**(2*dataWidth-rngSeqLengthLog-leftshit_2-leftshit_1)))
    return torch.tensor(resultBinary)


def getMemorySpace(tensor_variable):

# 获取Tensor数据占用的内存大小（以字节为单位）
    data_size_in_bytes = tensor_variable.element_size() * tensor_variable.numel()

# 将字节大小转换为更常见的单位，如千兆字节（MB）
    data_size_in_megabytes = data_size_in_bytes / (1024**2)
    return data_size_in_megabytes

def matrixMulSC(tensorData_1 , tensorData_2 , rngSeq , dataWidth , device):
    startTime = time.time()
    bitstreamLength = len(rngSeq)
    ascendingSeq = torch.tensor([x for x in range(bitstreamLength)]).to(device)
    enlargedData_1 , dataLeftShiftTime_1 =  TensorEnlargeModule(tensorData=abs(tensorData_1), dataWidth=dataWidth)
    enlargedData_2 , dataLeftShiftTime_2 =  TensorEnlargeModule(tensorData=abs(tensorData_2), dataWidth=dataWidth)
    dataShape_1 = tensorData_1.size()
    dataShape_2 = tensorData_2.size()
    signData_1 =  torch.sign(tensorData_1)
    signData_2 =  torch.sign(tensorData_2)
    '''
    Begin:将数据维度转换成合适shape
    '''
    dataLeftShiftTime_1 = (dataLeftShiftTime_1.unsqueeze(1)).repeat(1,dataShape_2[1],1)
    dataLeftShiftTime_2 = (dataLeftShiftTime_2.unsqueeze(0)).repeat(dataShape_1[0],1,1)
    dataLeftShiftTime_2 = torch.transpose(input=dataLeftShiftTime_2,dim0=1,dim1=2)
    dataScaledTime =  2*dataWidth -( dataLeftShiftTime_1 + dataLeftShiftTime_2) - math.log2(bitstreamLength)
    del dataLeftShiftTime_1
    del dataLeftShiftTime_2

    tensorBit_1 = tensorGenBitstreamMulti(rngSeq = rngSeq , tensorInputData= enlargedData_1 , dataWidth= dataWidth).to(device)
    tensorBit_2 = tensorGenBitstreamMulti(rngSeq = ascendingSeq , tensorInputData= enlargedData_2 , dataWidth= dataWidth).to(device)
    tensorBit_1 = tensorBit_1.to(torch.float16)
    tensorBit_2 = tensorBit_2.to(torch.float16)
    torch.mul(input=tensorBit_1, other=(signData_1.unsqueeze(2).repeat(1,1,bitstreamLength)),out=tensorBit_1)
    torch.mul(input=tensorBit_2, other=(signData_2.unsqueeze(2).repeat(1, 1, bitstreamLength)), out=tensorBit_2)

    del signData_1
    del signData_2

    '''
        End:将数据维度转换成合适shape
    '''


    tensorBit_1 = tensorBit_1.unsqueeze(1).expand(-1, dataShape_2[1],-1,-1)
    tensorBit_2 = tensorBit_2.unsqueeze(0).expand(dataShape_1[0], -1, -1, -1)
    tensorBit_2 = tensorBit_2.transpose(1, 2).transpose(2, 3)

    # 执行矩阵乘法

    SCResult = (tensorBit_1).matmul(tensorBit_2)

    del tensorBit_1
    del tensorBit_2

    SCResultDiagonal =  torch.diagonal(input= SCResult,dim1=2,dim2=3)
    SCResultDiagonal = SCResultDiagonal.mul(2**dataScaledTime)
    SCMatrixResult = torch.sum(input=SCResultDiagonal,dim=2)
    # print(SCMatrixResult)
    endTime = time.time()
    print(f"Parallel MulSC cost time : {endTime - startTime}")

    return SCMatrixResult

    # exactResult =


def splitTensor(tensorA, num_slices):
    m, n = tensorA.shape

    # 计算每个子张量的宽度
    width = n // num_slices

    # 初始化一个空列表，用于存储切片后的子张量
    sliced_tensors = []

    # 循环生成切片
    for i in range(num_slices):
        start_col = i * width
        end_col = (i + 1) * width if i < num_slices - 1 else n
        sliced_tensor = tensorA[:, start_col:end_col]
        sliced_tensors.append(sliced_tensor)

    return sliced_tensors






def matrixMulSeriesSC_new(tensorData_1 , tensorData_2 , SobolSeq1 , SobolSeq2,AscendingSeq , dataWidth , device):
    bitstreamLength = len(SobolSeq1)
    enlargedData_1 , dataLeftShiftTime_1 =  TensorEnlargeModule(tensorData=abs(tensorData_1), dataWidth=dataWidth)
    enlargedData_2 , dataLeftShiftTime_2 =  TensorEnlargeModule(tensorData=abs(tensorData_2), dataWidth=dataWidth)
    '''
    Begin:将数据维度转换成合适shape
    '''
    dataScaledFactor =(2**((2*dataWidth - math.log2(bitstreamLength) - dataLeftShiftTime_2 - dataLeftShiftTime_1).to(torch.float64))).to( torch.float64)

    # SCResult = torch.empty((dataShape_1[0],dataShape_2[1]),dtype=torch.float)
    res_Stochastic = torch.zeros_like(enlargedData_1).to(device).to(torch.float64)
    res_Unary = torch.zeros_like(enlargedData_1).to(device).to(torch.float64)

    for i in range (bitstreamLength):
        tensorBit_1 = tensorGenBitstreamSeries(rngSeq = SobolSeq1 , tensorInputData= enlargedData_1 , index= i , dataWidth= dataWidth).to(device)
        tensorBit_2 = tensorGenBitstreamSeries(rngSeq = SobolSeq2 , tensorInputData= enlargedData_2 ,index= i , dataWidth= dataWidth).to(device)
        asendingBit_3 = tensorGenBitstreamSeries(rngSeq=AscendingSeq, tensorInputData=enlargedData_2, index=i,
                                               dataWidth=dataWidth).to(device)

        tensorBit_1 = tensorBit_1.to(torch.int8)
        tensorBit_2 = tensorBit_2.to(torch.int8)
        tensorBit_3 = asendingBit_3.to(torch.int8)
        res_Stochastic = res_Stochastic + (torch.bitwise_and(tensorBit_1 , tensorBit_2)).to(torch.int32)
        res_Unary = res_Unary + (torch.bitwise_and(tensorBit_1 , tensorBit_3)).to(torch.int32)

    res_Unary  = res_Unary  * dataScaledFactor
    res_Unary  = res_Unary .to(torch.int32)

    res_Stochastic = res_Stochastic * dataScaledFactor
    res_Stochastic = res_Stochastic.to(torch.int32)
    return res_Stochastic , res_Unary



def TensorSC_MUL(tensorData_1 , tensorData_2 , rngSeq , dataWidth , device):
    bitstreamLength = len(rngSeq)
    ascendingSeq = torch.tensor([x for x in range(bitstreamLength)]).to(device)
    enlargedData_1, leftShift_1 = TensorEnlargeModule(tensorData=abs(tensorData_1),dataWidth= dataWidth)
    enlargedData_2, leftShift_2 = TensorEnlargeModule(tensorData=abs(tensorData_2), dataWidth=dataWidth)
    signTensorData_1 =  torch.sign(tensorData_1)
    signTensorData_2 =  torch.sign(tensorData_1)


    opA = torch.ones_like(leftShift_1) * 2<<(dataWidth - leftShift_1.to(torch.int ) - 1)
    opB = torch.ones_like(leftShift_2) * 2<<(dataWidth - leftShift_2.to(torch.int ) - 1)
    # opResult = opA + opB

    tensorResult = torch.zeros(enlargedData_1.size(0),enlargedData_2.size(1),enlargedData_2.size(0)).to(tensorData_1.device)
    for i in range(bitstreamLength ):
        tensorBitstream_1 = TensorGenBitstream(rngSeq, tensorInputData= enlargedData_1,index= i, dataWidth=dataWidth)
        tensorBitstream_2 = TensorGenBitstream(ascendingSeq, tensorInputData=enlargedData_2, index=i, dataWidth=dataWidth)
        for i in range(tensorBitstream_1.size(0)):
            for j in range(tensorBitstream_2.size(1)):
                a = tensorBitstream_1[i,:]
                b = tensorBitstream_2.t()[j,:]
                dataA = opA[i,:]
                dataB = opB.t()[j,:]
                signA = signTensorData_1[i,:]
                signB = signTensorData_2.t()[j,:]
                tensorResult[i,j,:]  +=  (dataB*signB+dataA*signA) * (a & b)


    for i in range(enlargedData_1.size(0)):
        for j in range(enlargedData_2.size(1)):
            tensorResult[i, j, :] += (dataB + dataA) * (a & b)

    tensorResult
    return enlargedData_2



#
if __name__ == "__main__":
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    sobol_1 = [0,8,12,4,6,14,10,2,3,11,15,7,5,13,9,1]
    sobol_2 = [0,8,4,12,6,14,2,10,5,13,1,9,3,11,7,15]
    sobol_3 = [0,8,4,12,10,2,14,6,15,7,11,3,5,13,1,9]
    sobol_4 = [0,8,4,12,14,6,10,2,7,15,3,11,9,1,13,5]
    sobol_5 = [0,8,12,4,6,14,10,2,9,1,5,13,15,7,3,11]
    sobol_6 = [0,8,12,4,2,10,14,6,5,13,9,1,7,15,11,3]
    sobol_7 = [0,8,4,12,6,14,2,10,7,15,3,11,1,9,5,13]
    sobol_8 = [0,8,12,4,14,6,2,10,15,7,3,11,1,9,13,5]
    # sobol_1 = [0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    # sobol_2 = [0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    # sobol_3 = [0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    # sobol_4 = [0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    # sobol_5 = [0,16,24,8,12,28,20,4,18,2,10,26,30,14,6,22,9,25,17,1,5,21,29,13,27,11,3,19,23,7,15,31]
    # sobol_6 = [0,16,24,8,4,20,28,12,10,26,18,2,14,30,22,6,31,15,7,23,27,11,3,19,21,5,13,29,17,1,9,25]
    # sobol_7 = [0,16,8,24,12,28,4,20,14,30,6,22,2,18,10,26,17,1,25,9,29,13,21,5,31,15,23,7,19,3,27,11]
    # sobol_8 = [0,16,24,8,28,12,4,20,30,14,6,22,2,18,26,10,27,11,3,19,7,23,31,15,5,21,29,13,25,9,1,17]
    # ascendingSeq = torch.tensor([x for x in range(bitstreamLength)]).to(device)
    # ascendingSeq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    ascendingSeq = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    # sobolTensor = torch.tensor(sobol_1).to(device)
    dataWidth = 16
    dim = 65535
    dim_1= int((dim+1)/128)

    # dim_1= dim
    dim_2 = dim
    REDsum = torch.zeros((dim_1,dim_2)).to(device).to(torch.float64)
    AEDsum = torch.zeros((dim_1,dim_2)).to(device).to(torch.float64)
    SeqType1 = [(sobol_1,sobol_2), (sobol_2,sobol_3),(sobol_3,sobol_4),(sobol_4,sobol_5),(sobol_5,sobol_6),(sobol_6,sobol_7),(sobol_7,sobol_8),(sobol_8,sobol_3)]
    # SeqType1 = [(sobol_1,sobol_2), (sobol_2,sobol_3)]
    # SeqType1 = [(sobol_1,sobol_2)]

    # SeqType2 = [(sobol_1, ascendingSeq), (sobol_2, ascendingSeq), (sobol_3, ascendingSeq), (sobol_4, ascendingSeq), (sobol_5, ascendingSeq),
    #             (sobol_6, ascendingSeq), (sobol_7, ascendingSeq), (sobol_8, ascendingSeq)]
    MREDGroup = []
    MEDGroup = []
    for tuples in SeqType1:
        SC_REDsum = 0
        SC_AEDsum = 0
        Unary_REDsum = 0
        Unary_AEDsum = 0
        for i in range(0,128):
            start = dim_1 * i
            end = dim_1 * (i+1)
            tensor1 = torch.arange(start+1, end+1,dtype=torch.int64).unsqueeze(1).expand(dim_1, dim_2).to(device)
            # tensor2 = torch.arange(1, dim + 1).unsqueeze(0).expand(int((dim+1)/64), dim)
            tensor2 = torch.arange(1, dim + 1,dtype=torch.int64).unsqueeze(0).expand(dim_1, dim_2).to(device)
            tensor1 = torch.where(tensor1<65535,tensor1,65535)
            (SCResult,UnaryResult )= matrixMulSeriesSC_new(tensorData_1=tensor1, tensorData_2=tensor2, SobolSeq1=tuples[0], SobolSeq2=tuples[1],AscendingSeq=ascendingSeq,
                                                    dataWidth=dataWidth, device=device)
            accurateRes= tensor1 * tensor2
                # print("***********\n\n")
            SC_RED = abs(1 - (SCResult.to(torch.float64) / accurateRes.to(torch.float64)))
            SC_ED = abs(SCResult.to(torch.float64) - accurateRes.to(torch.float64))/(65536*65536)
            Unary_RED = abs(1 - (UnaryResult.to(torch.float64) / accurateRes.to(torch.float64)))
            Unary_ED = abs(UnaryResult.to(torch.float64) - accurateRes.to(torch.float64)) / (65536 * 65536)

            SC_REDsum += SC_RED
            SC_AEDsum += SC_ED

            Unary_REDsum += Unary_RED
            Unary_AEDsum += Unary_ED
            print(i)
            # if(i==63):
            #     print(1)
        SC_RED = torch.sum(SC_REDsum)/(65535*65535)
        SC_ED = torch.sum (SC_AEDsum)/(65535*65535)
        Unary_RED = torch.sum(Unary_REDsum) / (65535 * 65535)
        Unary_ED = torch.sum(Unary_AEDsum) / (65535 * 65535)
        MREDGroup.append((SC_RED,Unary_RED))
        MEDGroup.append((SC_ED, Unary_ED))
    print(MREDGroup)
    print(MEDGroup)
    fileName = open('res_16precision_16bitstream.txt', mode='w+')
    fileName.write("MRED:\n")
    for data in MREDGroup:
        writeLine = ("\t"+str(data[0].item()) +","+str(data[1].item())+"\n" )
        fileName.write(writeLine)
    fileName.write("MED:\n")
    for data in MEDGroup:
        writeLine = ("\t"+str(data[0].item()) +","+str(data[1].item()) +"\n")
        fileName.write(writeLine)
    fileName.close()