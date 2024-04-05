import os
import random
import string

#generate_random_alphabet
def GRA():
  alphabet = list(string.ascii_lowercase)
  random.shuffle(alphabet)
  return ''.join(alphabet)

def encrypt(message, key):
  os.system("clear")
  alpha = "abcdefghijklmnopqrstuvwxyz"
  EMessage = ""
    
  for char in message:
    if char in alpha:
      char_index = alpha.index(char)
      EMessage += key[char_index]
    else:
      EMessage += char
    
  return EMessage

def decrypt(EMessage, key):
  os.system("clear")
  alpha = "abcdefghijklmnopqrstuvwxyz"
  DMessage = ""

  for char in EMessage:
    if char in key:
      char_index = key.index(char)
      DMessage += alpha[char_index]
    else:
      DMessage += char

  return DMessage

#Start of program
print("Welcome to Substitiution Cipher\n")

print("Would you like to encrypt or decrypt?")

ans = input("Type 'e' for encrypt and 'd' for decrypt: ")

print("\nProvide the Message: ")
mgs = input("[str]: ")

print("\nDo you have a key or would you like to generate one?")
KEY = ""
ANS = input("Type 'k' for key or 'g' for generate: ")

if ANS == 'k':
  KEY = input("Enter your key[in format of mapping]: ")
elif ANS == 'g':
  KEY = GRA()
else:
  print("Invalid input")
  exit(2)

if ans == 'e':
  EM = encrypt(mgs, KEY)
  print("Encrypted Message: " + EM)
  print("Key used: " + KEY)
elif ans == 'd':
  DM = decrypt(mgs, KEY)
  print("Decrypted Message: " + DM)
  print("Key used: " + KEY)
else:
  print("Invalid input")
  exit(0)