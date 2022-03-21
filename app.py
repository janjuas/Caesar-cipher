from tkinter import *
from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'," ", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'," "]

root = Tk()
root.title("caesar cipher")
# root.columnconfigure(1, weight=2)
# root.rowconfigure(1, weight=2)


# Encryption function
def encrypt():
    text = message_entry.get().lower()
    shift = int(shift_entry.get())

    # Shifting the Alphabet list by the shift amount
    shift_alpha = deque(alphabet)
    shift_alpha.rotate(shift)
    shift_alpha = list(shift_alpha)

    cipher_text = []
    for letter in text:
        index = alphabet.index(letter)
        cipher_text.append(shift_alpha[index])  # Grabbing the matching index letter from the shifted Alphabet list.
    output = ''.join(cipher_text)
    result_entry.delete(0, END)
    result_entry.insert(0, output)  # Displaying the result in Entry box


# Decryption function
def decrypt():
    text = message_entry.get().lower()
    shift = int(shift_entry.get())

    shift_alpha = deque(alphabet)
    shift_alpha.rotate(shift * -1)
    shift_alpha = list(shift_alpha)

    cipher_text = []
    for letter in text:
        index = alphabet.index(letter)
        cipher_text.append(shift_alpha[index])
    output = ''.join(cipher_text)
    result_entry.delete(0, END)
    result_entry.insert(0, output)


# Creating the text labels for each entry box
message_label = Label(root, text="Message ").grid(row=0, column=0, sticky="e")
shift_label = Label(root, text="Shift Factor ").grid(row=1, column=0, sticky="e")
result_label = Label(root, text="Result ").grid(row=2, column=0, sticky="e")

# Creating Entry boxes
message_entry = Entry(root, width=25)
message_entry.grid(row=0, column=1, padx=0, pady=5)

shift_entry = Entry(root, width=25)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

result_entry = Entry(root, width=25)
result_entry.grid(row=2, column=1, padx=5, pady=5)

# Creating action buttons to Encrypt or Decrypt messages
encrypt_button = Button(root, text="Encrypt", command=encrypt, width=15,anchor=CENTER)
encrypt_button.grid(row=3, column=0, sticky="e", padx=10)

decrypt_button = Button(root, text="Decrypt", command=decrypt, width=15,anchor=CENTER)
decrypt_button.grid(row=3, column=1, sticky="w", padx=10)

root.mainloop()
