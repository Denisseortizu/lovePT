"""
Author: Denisse Ortiz
Date of creation: 27/02/2024
Last modification: 28/02/2024
Description: Program for writting love letters out of given txt

Other Information:
- Version: 1.01
- Contact: hello.denisseortiz@example.com
"""

import markovify

##First we init out text file
with open("love.txt", 'r', encoding="utf-8") as file:
    textos = file.read()
    


modelo = markovify.Text(textos, state_size=3)
print(modelo.make_sentence(tries=100))

"""for _ in range(2):
    print(modelo.make_sentence(tries=100))
    oraciones = []
    for _ in range(5):  
        oracion = modelo.make_sentence()
    
        if oracion:
            oraciones.append(oracion)
    paragraph = " ".join(oraciones)
    #print(paragraph)
    #print("\n")"""



