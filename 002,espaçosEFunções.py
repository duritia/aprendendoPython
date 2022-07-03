"""
Entendendo mais da sintaxe da linguagem Python: espaços e quebras de linha para
formatar argumentos de funções

Discussão: https://www.linuxquestions.org/questions/programming-9/python-syntax-problem-4175714185/
"""
import sqlite3
import sys
from subprocess import call

call( ['rm', '-frv', 'bancoTeste'] )    # Apaga o arquivo existente, se existir

con = sqlite3.connect( "bancoTeste" )   # Cria um arquivo novo, vazio
bd = con.cursor()                       # Prepara para operar nele

bd.execute \
(
    # Cria tabela com uma única coluna do tipo 'texto'
    "create table tabeleste (   coleste         text )" 
)

bd.execute( "insert into tabeleste values (datetime())" )

con.commit()
con.close()

print( 'fim?' )

# vim: fileencoding=utf-8: expandtab: shiftwidth=4: tabstop=8: softtabstop=4
