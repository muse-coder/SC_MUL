def decimal_to_fixed_width_binary(decimal_number, width):
    binary_representation = bin(decimal_number)[2:]  # 获取二进制表示，去除前缀'0b'
    if len(binary_representation) < width:
        # 如果二进制表示位数小于指定宽度，在左侧填充0直到达到指定宽度
        binary_representation = '0' * (width - len(binary_representation)) + binary_representation
    elif len(binary_representation) > width:
        # 如果二进制表示位数大于指定宽度，截取右侧的位数，保留最右边的width位
        binary_representation = binary_representation[-width:]
    return binary_representation


sobol_1=[0,16,24,8,12,28,20,4,6,22,30,14,10,26,18,2,3,19,27,11,15,31,23,7,5,21,29,13,9,25,17,1]
sobol_2=[0,16,8,24,12,28,4,20,10,26,2,18,6,22,14,30,15,31,7,23,3,19,11,27,5,21,13,29,9,25,1,17]


fileName=open('sobol.txt',mode='w+')
for item in sobol_2:
    number = decimal_to_fixed_width_binary(item,5)
    fileName.write(number+'\n')
fileName.close()