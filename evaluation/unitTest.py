from SC_MUL.components import *
import pandas as pd
import statistics
import os
import math
if __name__=="__main__":
	sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
	sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]
	sobol_3=[0,16,8,24,20,4,28,12,30,14,22,6,10,26,2,18,15,31,7,23,27,11,19,3,17,1,25,9,5,21,13,29]
	sobol_4=[0,16,8,24,28,12,20,4,14,30,6,22,18,2,26,10,21,5,29,13,9,25,1,17,27,11,19,3,7,23,15,31]

###	#####################################################                       
	dataWidth = 16                                    ###        
	sobolWidth = int(math.log(len(sobol_1),2))        ###       
	validSegWidth = sobolWidth                      ###
	# validSegWidth = 16                              ###
	dataRange=(1,pow(2,16))                           ###
	iterationRange=1                     ###
	num_1=18
	num_2=21

#########################################################
	group_1=[sobol_1,sobol_2]
	sobolGroups=[group_1]
	sequence = [1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,1]
	sequence_re=list(reversed(sequence))
	# print(sequence_re)
	apc = approximate_APC_16(sequence)
	accurate_apc =accurate_APC(sequence)
	reverse_apc = approximate_APC_16(sequence_re)
	reverse_accurate_apc =accurate_APC(sequence_re)
	print(apc)
	print(reverse_apc)
	print(accurate_apc)
