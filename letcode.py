#1. diccionarios
#1768. Merge Strings Alternately

#Se le dan dos cadenas word1y word2. Combine las cadenas añadiendo letras en orden alterno, comenzando con word1. Si una cadena es más larga que otra, añada las letras adicionales al final de la cadena fusionada.

# Devuelve la cadena fusionada.

 

# Ejemplo 1:

# Entrada: palabra1 = "abc", palabra2 = "pqr"
#  Salida: "apbqcr"
#  Explicación:  La cadena fusionada se fusionará de la siguiente manera:
# palabra1: abc
# palabra2: pqr
# fusionado: apbqcr
# Ejemplo 2:

# Entrada: palabra1 = "ab", palabra2 = "pqrs"
#  Salida: "apbqrs"
#  Explicación:  Observe que como palabra2 es más larga, se agrega "rs" al final.
# palabra1: ab
# palabra2: pqrs
# fusionado: apbqrs
# Ejemplo 3:

# Entrada: palabra1 = "abcd", palabra2 = "pq"
#  Salida: "apbqcd"
#  Explicación:  Observe que como palabra1 es más larga, "cd" se agrega al final.
# palabra1: abcd
# palabra2: pq
# fusionado: apbqcd
 

# Restricciones:

# 1 <= word1.length, word2.length <= 100
# word1y word2constan de letras minúsculas en inglés.


def mergeAlternately(word1: str, word2: str) -> str:
        dicti = {word1:word2}
        word = ""
        
        for i in range(len(word1) if len(word1)<len(word2) else len(word2)):
            for key, value in dicti.items():
                word += key[i]+value[i]

        
        new_word2 = (word2[len(word1):len(word2)] if  len(word1)<len(word2) else word1[len(word2):len(word1)])       
        return word+new_word2


#dicti = {word1[i]:word2[i] for i in range(len(word1))}



print(mergeAlternately("meandro", "hola"))

def mergeAlternately2( word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        print('------------------------',merged)
        #------------------------ ['mh', 'eo']
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)

print(mergeAlternately2("me", "hola"))
#mheola
print("-----------------------------------")


def mergeAlternately3( word1: str, word2: str) -> str:
        merged = []
        new_word = ""
        print(dict(zip(word1, word2)))
        #{'m': 'h', 'e': 'o'}


print('3',mergeAlternately3("me", "hola"))

print("-------------------------------------------------")

worda = "anarkis"
wordb = "mew"

def mergeAlternately4( word1: str, word2: str) -> str:

    new_word = ""
    for i in range(min(len(word1), len(word2))):
        new_word += '{0}{1}'.format(word1[i], word2[i]) 

    new_word += (word1[len(word2):] if len(word1)>len(word2) else word2[len(word1):])

    return new_word

print(mergeAlternately4("me", "hola"))
#mheola

