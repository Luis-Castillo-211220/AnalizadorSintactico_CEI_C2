import tkinter as tk
from tkinter import ttk, messagebox
import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = [
    'AS',
    'PA',
    'PC',
    'CM',
    # 'CC',
    'CO',
    'LA',
    'LC',
    'OR',
    'TP',
    'ID',
    'NUMBER'
]

# Define reserved words
reserved = {
    'int': 'TP',
    'string': 'TP',
    'Fn': 'F',
    # 'contenido': 'C',
    'print': 'PRT',
    'if': 'I',
    'else': 'E',
    'while': 'W',
    'switch': 'SW',
    'case': 'CE',
    'default': 'DT',
    'break': 'BR',
    'rtn': 'RT',
}

tokens += list(reserved.values())

errores = []

# t_TP = r'int|string'
t_PA = r'\('
t_PC = r'\)'
t_LA = r'\{'
t_LC = r'\}'
t_CM = r'"'
# t_CC = r'"'
t_CO = r','
t_AS = r'=>'
t_OR = r'(>=|<=|==|!=|>|<)'

def t_ID(t):
    # r'[a-zA-Z_][a-zA-Z_0-9]*'
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# def p_empty(p):
#     'empty :'
#     pass

t_ignore = ' \t\n'

def t_error(t):
    mensaje_error = f"Carácter ilegal '{t.value[0]}'"
    errores.append(mensaje_error)
    t.lexer.skip(1)

lexer = lex.lex()

def p_PX(p):
    '''PX : V
            | RF
            | RI
            | RW
            | S'''
#VARIABLES
def p_V(p):
    '''V : ID AS TP VL'''
        
#FUNCION                
def p_RF(p):
    '''RF : F AS ID PR LA C R LC'''

#IF-ELSE               
def p_RI(p):
    '''RI : I CD AS LA C LC RE'''

#WHILE 
def p_RW(p):
    '''RW : W CD AS LA C LC'''
    
#SWITCH    
def p_S(p):
    '''S : SW OP AS LA CA RCA DF LC'''
                 
#PRODUCCIONES    
def p_VL(p):
    '''VL : PA CM ID CM PC
                 | PA NUMBER PC
                 | '''
          
def p_P(p):
    '''P : TP ID
                 | '''
    
def p_PR(p):
    '''PR : PA P RP PC'''
    
def p_RP(p):
    '''RP : CO P RP
            | '''
    
def p_CD(p):
    '''CD : PA ID OR RC PC'''
    
def p_RC(p):
    '''RC : ID
            | NUMBER'''

def p_RE(p):
    '''RE : E AS LA C LC
            | '''
                  
def p_OP(p):
    '''OP : PA ID PC'''
    
def p_CA(p):
    '''CA : CE NUMBER AS LA C BR LC'''
    
def p_RCA(p):
    '''RCA : CA RCA
            | '''
            
def p_DF(p):
    '''DF : DT AS LA C LC'''
    
def p_R(p):
    '''R : RT ORT
            | '''
            
def p_ORT(p):
    '''ORT : PA CM ID CM PC
            | PA ID PC
            | PA  NUMBER PC'''
                                       
def p_C(p):
    '''C : PRT ORT'''
            
def p_error(p):
    if p:
        errores.append(f"Error de sintaxis en '{p.value}'")
    else:
        errores.append("Error de sintaxis al final de la entrada")

parser = yacc.yacc()
            
# def lex_analysis(code):
#     lexer = lex.lex()
#     lexer.input(code)

# def syntax_analysis(code):
#     lexer = lex.lex()
#     parser = yacc.yacc()
#     errors = []
            
#     result = parser.parse(code, lexer=lexer)
#     return errors

def analizar(texto):
    # Asegúrate de limpiar la lista de errores antes de cada análisis
    errores.clear()
    lexer.input(texto)
    tokens = []
    for token in lexer:
        tokens.append((token.type, token.value))
    parser.parse(texto)
    # Retorna la lista de errores para que pueda ser usada por la interfaz gráfica
    return errores, tokens