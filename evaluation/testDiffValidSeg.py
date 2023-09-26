from SC_MUL.components import *
import pandas as pd
import statistics
import os
import math
def generate_df(mredGroup  , segRange ,savingPath ):
    # dfIndex=[]
    dfMred=[]
    dfValidSegWidth=[]
    for i in range(segRange[0],segRange[1]):
        # print(pattern_name)
        # dfIndex.append(("ValidSegmentRange_"+str(i)))
        mred = "%.4lf"%(mredGroup[i-segRange[0]]*100)+"%"
        dfMred.append(mred)
        dfValidSegWidth.append(i)

    data={"MRED:":dfMred ,"ValidSegmentWidth":dfValidSegWidth}
    df=pd.DataFrame(data)
    # file_path_split=file_path.split('\\')
    print("***********************************")
    print(df)
    # print(file_path)
    print("***********************************")
    print(os.getcwd())
    
    # to_csv_path="./evaluation/result/ValidSegResult_"+str(pow(2,sobolWidth))+".csv"
    to_excel_path="./evaluation/result/testDiffValidSeg.xls"
    df.to_csv(savingPath)
    # df.to_excel(to_csv_path,index=False)
    return df
    

if __name__=="__main__":
    sobol_1 = [0,4,6,2,3,7,5,1]
    sobol_2 = [0,4,2,6,3,7,1,5]
    sobol_3 = [0,4,2,6,5,1,7,3]
    sobol_4 = [0,4,2,6,7,3,5,1]
    sobol_1 = [0,8,12,4,6,14,10,2,3,11,15,7,5,13,9,1]
    sobol_2 = [0,8,4,12,6,14,2,10,5,13,1,9,3,11,7,15]
    sobol_3 = [0,8,4,12,10,2,14,6,15,7,11,3,5,13,1,9]
    sobol_4 = [0,8,4,12,14,6,10,2,7,15,3,11,9,1,13,5]
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    sobol_1=  [0,32,48,16,24,56,40,8,12,44,60,28,20,52,36,4,6,38,54,22,30,62,46,14,10,42,58,26,18,50,34,2,3,35,51,19,27,59,43,11,15,47,63,31,23,55,39,7,5,37,53,21,29,61,45,13,9,41,57,25,17,49,33,1]
    sobol_2=  [0,32,16,48,24,56,8,40,20,52,4,36,12,44,28,60,30,62,14,46,6,38,22,54,10,42,26,58,18,50,2,34,17,49,1,33,9,41,25,57,5,37,21,53,29,61,13,45,15,47,31,63,23,55,7,39,27,59,11,43,3,35,19,51]
    sobol_3=  [0,32,16,48,40,8,56,24,60,28,44,12,20,52,4,36,30,62,14,46,54,22,38,6,34,2,50,18,10,42,26,58,45,13,61,29,5,37,21,53,17,49,1,33,57,25,41,9,51,19,35,3,27,59,11,43,15,47,31,63,39,7,55,23]
    sobol_4=  [0,32,16,48,56,24,40,8,28,60,12,44,36,4,52,20,42,10,58,26,18,50,2,34,54,22,38,6,14,46,30,62,35,3,51,19,27,59,11,43,63,31,47,15,7,39,23,55,9,41,25,57,49,17,33,1,21,53,5,37,45,13,61,29]
    # sobol_1=[0,64,96,32,48,112,80,16,24,88,120,56,40,104,72,8,12,76,108,44,60,124,92,28,20,84,116,52,36,100,68,4,6,70,102,38,54,118,86,22,30,94,126,62,46,110,78,14,10,74,106,42,58,122,90,26,18,82,114,50,34,98,66,2,3,67,99,35,51,115,83,19,27,91,123,59,43,107,75,11,15,79,111,47,63,127,95,31,23,87,119,55,39,103,71,7,5,69,101,37,53,117,85,21,29,93,125,61,45,109,77,13,9,73,105,41,57,121,89,25,17,81,113,49,33,97,65,1]
    # sobol_2=[0,64,32,96,48,112,16,80,40,104,8,72,24,88,56,120,60,124,28,92,12,76,44,108,20,84,52,116,36,100,4,68,34,98,2,66,18,82,50,114,10,74,42,106,58,122,26,90,30,94,62,126,46,110,14,78,54,118,22,86,6,70,38,102,51,115,19,83,3,67,35,99,27,91,59,123,43,107,11,75,15,79,47,111,63,127,31,95,39,103,7,71,23,87,55,119,17,81,49,113,33,97,1,65,57,121,25,89,9,73,41,105,45,109,13,77,29,93,61,125,5,69,37,101,53,117,21,85]

    # sobol_1=[0,128,192,64,96,224,160,32,48,176,240,112,80,208,144,16,24,152,216,88,120,248, 184,56,40,168,232,104,72,200,136,8,12,140,204,76,108,236,172,44,60,188,252,124,92,220,156,28,20,148,212,84,116,244,180,52,36,164,228,100,68,196,132,4,6,134,198,70,102,230,166,38,54,182,246,118,86,214,150,22,30,158,222,94,126,254,190,62,46,174,238,110,78,206,142,14,10,138,202,74,106,234,170,42,58,186,250,122,90,218,154,26,18,146,210,82,114,242,178,50,34,162,226,98,66,194,130,2,3,131,195,67,99,227,163,35,51,179,243,115,83,211,147,19,27,155,219,91,123,251,187,59,43,171,235,107,75,203,139,11,15,143,207,79,111,239,175,47,63,191,255,127,95,223,159,31,23,151,215,87,119,247,183,55,39,167,231,103,71,199,135,7,5,133,197,69,101,229,165,37,53,181,245,117,85,213,149,21,29,157,221,93,125,253,189,61,45,173,237,109,77,205,141,13,9,137,201,73,105,233,169,41,57,185,249,121,89,217,153,25,17,145,209,81,113,241,177,49,33,161,225,97,65,193,129,1]
    # sobol_2=[0,128,64,192,96,224,32,160,80,208,16,144,48,176,112,240,120,248,56,184,24,152,88,216,40,168,104,232,72,200,8,136,68,196,4,132,36,164,100,228,20,148,84,212,116,244,52,180,60,188,124,252,92,220,28,156,108,236,44,172,12,140,76,204,102,230,38,166,6,134,70,198,54,182,118,246,86,214,22,150,30,158,94,222,126,254,62,190,78,206,14,142,46,174,110,238,34,162,98,226,66,194,2,130,114,242,50,178,18,146,82,210,90,218,26,154,58,186,122,250,10,138,74,202,106,234,42,170,85,213,21,149,53,181,117,245,5,133,69,197,101,229,37,165,45,173,109,237,77,205,13,141,125,253,61,189,29,157,93,221,17,145,81,209,113,241,49,177,65,193,1,129,33,161,97,225,105,233,41,169,9,137,73,201,57,185,121,249,89,217,25,153,51,179,115,243,83,211,19,147,99,227,35,163,3,131,67,195,75,203,11,139,43,171,107,235,27,155,91,219,123,251,59,187,119,247,55,183,23,151,87,215,39,167,103,231,71,199,7,135,15,143,79,207,111,239,47,175,95,223,31,159,63,191,127,255]

####################################################
    dataWidth = 6                               ###
    sobolWidth = int(math.log(len(sobol_1),2))                              ###
    dataRange=(1,pow(2,dataWidth))                      ###
    iterationRange=dataRange[1] * dataRange[1]                  ###
    # validSegWidth = 16                         ###                
    # writer = pd.ExcelWriter('test.xlsx')       ###
    segRange = (sobolWidth,dataWidth+1)                   ###
####################################################

    group_1=[sobol_1,sobol_2]
    # group_2=[sobol_1,sobol_3]
    # group_3=[sobol_1,sobol_4]
    # group_4=[sobol_2,sobol_3]
    # group_5=[sobol_2,sobol_4]
    # group_6=[sobol_3,sobol_4]
    
    workingPath = os.getcwd()
    
    savingPath=workingPath+'/evaluation/result'
    if not (os.path.exists(savingPath)):
        # savingPath=workingPath+'/result'
        os.mkdir(savingPath)
    
    savingPath = savingPath +'/testDiffValidSeg'
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)
        
    savingPath = savingPath +'/dataRange_1_to_'+str(dataRange[1])
    if not (os.path.exists(savingPath)):
        os.mkdir(savingPath)

    resultName = "sobol_%d.csv"%(pow(2,sobolWidth))
    savingPath = savingPath + '/'+ resultName

    mredGroup = []
    for i in range (segRange[1]-segRange[0]):
        mredGroup.append(0)
    
    for test in range(iterationRange):
        # num_1=random.randint(int(dataRange[1]>>sobolWidth),int(dataRange[1]))
        # num_2=random.randint(int(dataRange[1]>>sobolWidth),int(dataRange[1]))
        num_1=random.randint(8,int(dataRange[1]))
        num_2=random.randint(8,int(dataRange[1]))
        exact_res=num_1*num_2
        # print("num1 = %d, num2 = %d,error = "%(num_1,num_2),end='')
        # print("num1=%d,num2=%d,exact_res=%d"%(num_1,num_2,exact_res))
        for validSegWidth in  range(segRange[0],segRange[1]):
            # print(validSegWidth)
            isc_res=scaled_mul(
                num_1=num_1,num_2=num_2,
                sobol_1= group_1[0],sobol_2= group_1[1],validSegWidth=validSegWidth,
                sobolWidth= sobolWidth,dataWidth=  dataWidth
            )
            error = abs(isc_res/(exact_res)-1)
            mredGroup[validSegWidth-segRange[0]]+=(error)
            # print(isc_res,error, end=' ')
        # print('\n')

    mredGroup = [mredGroup [i] /iterationRange for i in range(len(mredGroup))]

    for i in range(len(mredGroup)):
        
        print("validSegWidth=%d  MRED  = %.4lf"%(int(segRange[0])+i,mredGroup[i]*100)+"% ")
    averageMRED = statistics.mean(mredGroup)
    print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")

    df = generate_df(mredGroup  , segRange  ,savingPath )
    # return mredGroup ,averageMRED
