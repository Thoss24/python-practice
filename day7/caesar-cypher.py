alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar():
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    text = input("Type message: ").lower()
    shift = int(input("Type the shift number: "))
    shifted = []
    for i in text:
        pos = alphabet.index(i)
        if direction == 'encode':
            new_pos = pos + shift
        else:
            new_pos = pos - shift
        shifted += alphabet[new_pos]
    print("".join(shifted))
    again = input("Type 'yes' to go again ").lower()
    if again == 'yes':
        shifted.clear()
        caesar()
    else: 
        return

caesar()
   

                