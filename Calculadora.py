import math as mt
class Calculator:
    def __init__(self):
        self.plusten = {
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15,
            'G':16
        }

        self.key = self.plusten.keys()

    def ten_ForBase(self,num,base):
        if type(num) == int:
            value = []
            number = num
            convertion = ''
            while abs(number) >= 1:
                element = number % base
                if base > 10 and element >= 10:
                    for chave in self.key:
                        if self.plusten[chave] == element:
                            element = chave
                value.append(element)
                number = int(number/base)
            
            value.reverse()

            for element in value:
                convertion += str(element)
            
            return convertion
        else:
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
                if base > 10 and element >= 10:
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
                flag2 = False
                mult = round(number_dec * base, 10)
                aux = mult
                if base > 10:
                    for chave in self.key:
                        if self.plusten[chave] == int(aux):
                            aux = chave
                            flag2 = True
                            break

                if flag2:
                    value_dec.append(aux)
                else:
                    value_dec.append(int(aux))

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


    def BaseFor10(self,num,base):
        string = str(num)
        if '.' not in string:
            string_int = []
            convertion = 0
            cont = 0

            for i in range(len(string)):
                if string[i] in self.key:
                    string_int.append(self.plusten[string[i]])
                else:
                    string_int.append(int(string[i]))
            
            for i in string_int:
                convertion += i * int(mt.pow(base,(len(string) - cont - 1)))
                cont +=1
                
            return convertion
        else:
            
            string_int = []
            convertion = 0
            n = 0
            cont = 0

            for i in range(len(string)):
                if string[i] == '.':
                    n = len(string_int) - 1
                    continue
                if string[i] in self.key:
                    string_int.append(self.plusten[string[i]])
                else:
                    string_int.append(int(string[i]))
            
            for i in string_int:
                convertion += i * mt.pow(base, (n- cont))
                cont = cont + 1
            
            return convertion
        
    def soma(self,num1,num2,base1,base2):
        number1 = self.BaseFor10(num1,base1)
        number2 = self.BaseFor10(num2,base2)
        print(number1)
        print(number2)
        soma = round(number1 + number2,5)

        print(f"SOMA NA BASE 10: {soma}")
        print(f"SOMA NA BASE {base1}: {self.ten_ForBase(soma,base1)}")
        print(f"SOMA NA BASE {base2}: {self.ten_ForBase(soma,base2)}")
        
    def subtraçao(self,num1,num2,base1,base2):
        number1 = self.BaseFor10(num1,base1)
        number2 = self.BaseFor10(num2,base2)
        print(number1)
        print(number2)
        soma = round(number1 - number2,5)

        print(f"SUBTRAÇÃO NA BASE 10: {soma}")
        print(f"SUBTRAÇÃO NA BASE {base1}: {self.ten_ForBase(soma,base1)}")
        print(f"SUBTRAÇÃO NA BASE {base2}: {self.ten_ForBase(soma,base2)}")
    
    def multiplication(self,num1,num2,base1,base2):
        number1 = self.BaseFor10(num1,base1)
        number2 = self.BaseFor10(num2,base2)
        print(number1)
        print(number2)
        soma = round(number1 * number2,5)

        print(f"MULTIPLICAÇÃO NA BASE 10: {soma}")
        print(f"MULTIPLICAÇÃO NA BASE {base1}: {self.ten_ForBase(soma,base1)}")
        print(f"MULTIPLICAÇÃO NA BASE {base2}: {self.ten_ForBase(soma,base2)}")

    def divisao(self,num1,num2,base1,base2):
        number1 = self.BaseFor10(num1,base1)
        number2 = self.BaseFor10(num2,base2)
        print(number1)
        print(number2)
        soma = round(number1 / number2,5)

        print(f"DIVISÃO NA BASE 10: {soma}")
        print(f"DIVISÃO NA BASE {base1}: {self.ten_ForBase(soma,base1)}")
        print(f"DIVISÃO NA BASE {base2}: {self.ten_ForBase(soma,base2)}")


 