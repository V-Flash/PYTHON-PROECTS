alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


ceaser_chipher = False

user_input = input("Do you want to use Ceaser-Chipher?(Y/N): ")

if user_input == "y" or user_input == "Y":
    ceaser_chipher = True
else:
    pass

while ceaser_chipher == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    # Create a function called 'encrypt' that takes the 'plaintext' and 'key' as inputs.
    def encrypt(plaintext,key):

        cipher_Text = ""

        for letter in plaintext:
            position = alphabet.index(letter)
            new_position = position + key
            new_letter = alphabet[new_position]
            cipher_Text += new_letter

        print(f"encrypt msg: {cipher_Text}")




    # Create a function called 'decrypt' that takes the 'cipher_text' and 'key' as inputs.
    def decrypt(cipher_text, key):
        plain_Text = ""

        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - key
            new_letter = alphabet[new_position]
            plain_Text += new_letter

        print(f"decrypt msg: {plain_Text}")


    if direction == "encode":
        encrypt(plaintext=text, key=shift)
    elif direction == "decode":
        decrypt(cipher_text=text, key=shift)
