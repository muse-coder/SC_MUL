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
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]
    # sobol_1=  [0,32,48,16,24,56,40,8,12,44,60,28,20,52,36,4,6,38,54,22,30,62,46,14,10,42,58,26,18,50,34,2,3,35,51,19,27,59,43,11,15,47,63,31,23,55,39,7,5,37,53,21,29,61,45,13,9,41,57,25,17,49,33,1]
    # sobol_2=  [0,32,16,48,24,56,8,40,20,52,4,36,12,44,28,60,30,62,14,46,6,38,22,54,10,42,26,58,18,50,2,34,17,49,1,33,9,41,25,57,5,37,21,53,29,61,13,45,15,47,31,63,23,55,7,39,27,59,11,43,3,35,19,51]
    # sobol_3=  [0,32,16,48,40,8,56,24,60,28,44,12,20,52,4,36,30,62,14,46,54,22,38,6,34,2,50,18,10,42,26,58,45,13,61,29,5,37,21,53,17,49,1,33,57,25,41,9,51,19,35,3,27,59,11,43,15,47,31,63,39,7,55,23]
    # sobol_4=  [0,32,16,48,56,24,40,8,28,60,12,44,36,4,52,20,42,10,58,26,18,50,2,34,54,22,38,6,14,46,30,62,35,3,51,19,27,59,11,43,63,31,47,15,7,39,23,55,9,41,25,57,49,17,33,1,21,53,5,37,45,13,61,29]

####################################################
    dataWidth = 16                               ###
    sobolWidth = int(math.log(len(sobol_1),2))                              ###
    dataRange=(1,pow(2,16))                      ###
    iterationRange=dataRange[1]                  ###
    # validSegWidth = 16                         ###                
    # writer = pd.ExcelWriter('test.xlsx')       ###
    segRange = (sobolWidth,17)                   ###
####################################################

    group_1=[sobol_1,sobol_2]
    group_2=[sobol_1,sobol_3]
    group_3=[sobol_1,sobol_4]
    group_4=[sobol_2,sobol_3]
    group_5=[sobol_2,sobol_4]
    group_6=[sobol_3,sobol_4]
    
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
        num_1=random.randint(dataRange[0],dataRange[1])
        num_2=random.randint(dataRange[0],dataRange[1])
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
