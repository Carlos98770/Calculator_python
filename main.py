import math as mt
class Calculator:
    def __init__(self):
        self.plusten = {
            'A':10,
            'B':11,
            'C':12,
            'D':13
        }

    def ten_ForBaseInt(self,num,base):
        value = []
        number = num
        conversion = ''
        while abs(number) >= 1:
            element = number % base
            value.append(element)
            number = int(number/base)
        
        value.reverse()

        for element in value:
            conversion += str(element)
        
        return int(conversion)

    def BaseFor10Int(self,num,base):
        string = str(num)
        conversion = 0
        for i in range(len(string)):
            conversion += int(string[i]) * int(mt.pow(base,(len(string) - i - 1)))
            
        return conversion
    
    def ten_ForBaseFloat(self,num,base):
        value_int = []
        value_dec = [',']
        number_int = int(num)
        number_dec = num - number_int
        part_int = ''

        if number_int == 0:
            value_int.append(0)

        #Algoritmo para parte INTEIRA
        while abs(number_int) >= 1:
            element = number_int % base
            value_int.append(element)
            number_int = int(number_int/base)
        
        value_int.reverse()

        for element in value_int:
            part_int += str(element)
        
        #Algoritmo para parte DECIMAL
        flag = True
        values = []
        while flag:
            mult = round(number_dec * base, 10)
            value_dec.append(int(mult))
            number_dec = mult - int(mult)
            values.append(number_dec)
            if len(values) != len(set(values)):
                value_dec.append('...')
                flag = False
                
            
            if number_dec == 0:
                flag = False
 
        for element in value_dec:
            part_int += str(element)
        
        return part_int



'''
Coisas a Fazer: Funcao de baseForTenFloat
solucionar quando a base for > 10
'''








