from SC_MUL.components import *
import pandas as pd
import statistics
import os
def generate_df(mredGroup  , segRange ,sobolWidth ):
    # dfIndex=[]
    dfMred=[]
    dfValidSegWidth=[]
    for i in range(segRange[0],segRange[1]):
        # print(pattern_name)
        # dfIndex.append(("ValidSegmentRange_"+str(i)))
        mred = "%.4lf"%(mredGroup[i-segRange[0]]*100)+"%"
        dfMred.append(mred)
        dfValidSegWidth.append(i)

    # averageMRED = statistics.mean(mredGroup)
    # dfIndex.append("averageMRED")
    # dfMred.append(averageMRED)
    # dfValidSegWidth.append(validSegWidth)
    # dfSobolWidth.append(sobolWidth)

    # print("\naverage MRED = %.4lf"%(averageMRED*100)+"%")
    data={"MRED:":dfMred ,"ValidSegmentWidth":dfValidSegWidth}
    df=pd.DataFrame(data)
    # file_path_split=file_path.split('\\')
    print("***********************************")
    print(df)
    # print(file_path)
    print("***********************************")
    print(os.getcwd())
    to_csv_path="./evaluation/result/ValidSegResult_"+str(pow(2,sobolWidth))+".csv"
    to_excel_path="./evaluation/result/testDiffValidSeg.xls"
    df.to_csv(to_csv_path)
    # df.to_excel(to_csv_path,index=False)
    return df
    

if __name__=="__main__":
    sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
    sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
    sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
    sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]

    dataWidth = 16
    sobolWidth = 5
    
    group_1=[sobol_1,sobol_2]
    group_2=[sobol_1,sobol_3]
    group_3=[sobol_1,sobol_4]
    group_4=[sobol_2,sobol_3]
    group_5=[sobol_2,sobol_4]
    group_6=[sobol_3,sobol_4]
    
    # sobolGroups=[group_1,group_2,group_3,group_4,group_5,group_6]
    # sobolGroups=[group_1]
    sobolGroups=[group_2]

    dataRange=(1,pow(2,8))     
    iterationRange=pow(2,5)*pow(2,5)
    # validSegWidth = 16
    # writer = pd.ExcelWriter('test.xlsx')
    segRange = (5,17)    
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

    df = generate_df(mredGroup  , segRange ,sobolWidth  )
    # return mredGroup ,averageMRED
