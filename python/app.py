#-Print
print('------------- Print ---------------------')
print('Welcome python!')
print('Hello')
print("Meu nome é lucas, minha idade é ", 30, 'anos')

#-Varibles
name = 'Lucas'
age = 30
 
print('------------- Variables -----------------')
print(name)
print(name + " is a boy")
print(name, "is",  age)
print(name + ' is from brazil')

#-strings
print('------------- Strings -----------------')
#name = "Lucas"
print('Hi,how are you?')
print('Hi,\nhow are you?') #quebra de texto
print(name)
print(name[3]) #pega a letra da string
print(name.upper()) #transforma em caixa alta .upper, .islower, .issupper
print(len(name))
print(name.index('a'))
print(name.replace("L", "C"))

#-numbers
print('------------- Numbers -----------------')
number = 55
print(23)
print(number + 23.56)
print(number - 23.56)
print(number / 23.56)
print(number * 23.56)

print(20%6)

number2 = str(number)
print('number is ' + number2)
print(max(4,2,3,16))
print(min(4,2,3,16))
print(round(3.5))
print(bin(3))

from math import *

print(sqrt(100))

#-Getting a user input
print('------------- Input -----------------')
name = input('Input Your Name: ')
age = int(input('Input Your Age: '))
print('Your name is ' + name + ' and you are', age, 'years old')

#-replace sentences
sentence = input('Enter your sentence:')
print('Your sentence is: ' + sentence)

word1 = input('Enter the word to replace: ')
word2 = input('Enter the word to replace it with: ')

print(sentence.replace(word1, word2))

#-lists
print('------------- Lists -----------------')
countries = ['United Kingdom', 'Brazil', 'Nigeria', 'EUA', 'Australia']

print(countries)
print(countries[1])
print(countries[1:4])
print(type(countries)) #type demonstra o tipo da variavel
print(countries[-1]) #pega o ultimo item da lista
print(len(countries))