'''
base cipher object that other ciphers extend
really only provides mappings a2i and i2a for letter->int->letter conversions
Author: James Lyons
Created: 2012-04-28
'''
import re

class Cipher(object):
    def encipher(self,string):
        return string
        
    def decipher(self,string):
        return string
        
    def a2i(self,ch):        
        return ord(ch.upper()) - ord('A')

    def i2a(self,i):        
        return chr(ord('A') + (i % 26))
        
    def remove_punctuation(self,text,filter='[^A-Z]'):
        return re.sub(filter,'',text.upper())
