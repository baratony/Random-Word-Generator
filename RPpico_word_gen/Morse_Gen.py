def String_To_Morse(str1):
    new_morse_string = []
    
    morse_code_alphabet = {
        "a": ".--",
        "b": "-...",
        "c": "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-.",
        "g" : "--.",
        "h" : "....",
        "i" : "..",
        "j" : ".---",
        "k" : "-.-",
        "l" : ".-..",
        "m" : "--",
        "n" : "-.",
        "o" : "---",
        "p" : ".--.",
        "q" : "--.-",
        "r" : ".-.",
        "s" : "...",
        "t" : "-",
        "u" : "..-",
        "v" : "...-",
        "w" : ".--",
        "x" : "-..-",
        "y" : "-.--",
        "z" : "--.." 
    }
    
    for i in range (len(str1)):
        new_morse_string.append(morse_code_alphabet.get(str1[i]))
        
    return (new_morse_string)