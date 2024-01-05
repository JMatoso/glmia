import re
from rich import print
from datetime import datetime

class Validations:
    @staticmethod
    def isnumber(value):
        if value.isdigit():
            return True
        else:
            print("[red]O valor introduzido não é um número válido![/red]\n")
            return False
            
    @staticmethod
    def isvalidtext(value, allow_empty = False):
        if (all(text.isalpha() for text in value.split())) == False:
            print("[red]O valor introduzido não é um texto válido![/red]\n")
            return False
        return True
        
    @staticmethod
    def isvalidemail(value):
        if len(value.strip()) <= 0 or value.isspace() or value.strip() == "" or value == None:
            return False
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if re.fullmatch(regex, value):
            return True
        else:
            print("[red]O valor introduzido não é um email válido![/red]\n")
            return False
        
    @staticmethod
    def isvaliddate(value):
        try:
            datetime.strptime(value, '%d/%m/%Y')
            return True
        except:
            print("[red]O valor introduzido não é uma data válida![/red]\n")
            return False
        
    @staticmethod
    def notempty(value):
        if len(value.strip()) <= 0 or value.isspace() or value.strip() == "" or value == None:
            print("[red]O valor introduzido não pode ser vazio![/red]\n")
            return False
        return True
    
    @staticmethod
    def isempty(value):
        if len(value.strip()) <= 0 or value.isspace() or value.strip() == "" or value == None:
            return True
        return False
    
    @staticmethod
    def normalize(value, isTitle = True):
        text = value.strip()
        text = ' '.join(text.split())
        if isTitle:
            text = text.title()
        return text
    
        