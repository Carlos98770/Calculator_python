import math as mt
class Calculator:
    def __init__(self):
        self.plusten = {
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15
        }

        self.key = self.plusten.keys()

    def ten_ForBaseInt(self,num,base):
        value = []
        number = num
        conversion = ''
        while abs(number) >= 1:
            element = number % base
            if base > 10 and element > 10:
                for chave in self.key:
                    if self.plusten[chave] == element:
                        element = chave
            value.append(element)
            number = int(number/base)
        
        value.reverse()

        for element in value:
            conversion += str(element)
        
        return conversion

    def BaseFor10Int(self,num,base):
        string = str(num)
        string_int = []
        conversion = 0
        cont = 0

        for i in range(len(string)):
            if string[i] in self.key:
                string_int.append(self.plusten[string[i]])
            else:
                string_int.append(int(string[i]))
        
        for i in string_int:
            conversion += i * int(mt.pow(base,(len(string) - cont - 1)))
            cont +=1
            
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
            if base > 10 and element > 10:
                for chave in self.key:
                    if self.plusten[chave] == element:
                        element = chave
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

'''






