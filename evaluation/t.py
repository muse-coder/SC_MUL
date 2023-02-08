from SC_MUL.components import *
import pandas as pd
import statistics
import time


def timestamp ( ):

  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return
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
    sobolGroups=[group_2]

    # writer = pd.ExcelWriter('test.xlsx')
    
    Set=[]
    segRange=(5,17)
    testRange=pow(2,9)*pow(2,9)
    dataRangeUpper=pow(2,9)
    dataRangeLower=1
    for i in range(segRange[0],segRange[1]):
        Set.append(0)
    timestamp()
    for test in range(testRange):
        num_1=random.randint(dataRangeLower,dataRangeUpper)
        num_2=random.randint(dataRangeLower,dataRangeUpper)
        # print("num1=%d ,num2=%d"%(num_1 ,num_2))
        for validSegWidth in range(segRange[0],segRange[1]):
            isc_res=scaled_mul(num_1=num_1,num_2=num_2, sobol_1= group_1[0],sobol_2= group_1[1],validSegWidth=validSegWidth,sobolWidth= sobolWidth,dataWidth=  dataWidth)
            error = abs(isc_res/(num_1*num_2)-1)
            Set[validSegWidth-segRange[0]]+=error
            # print("%.4lf i=%d"%(error ,i),end= ';')
        # print('\n')    
    for i in range(len(Set)):
        print("SegWidth=%d  average error = %.4lf"%(i+segRange[0],Set[i]/testRange*100)+"%",end= '\n')
    timestamp()
    # print(1111)
