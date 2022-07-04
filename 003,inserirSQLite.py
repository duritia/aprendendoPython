"""
Programa mínimo para inserção de dados no SQLite
"""

import sqlite3                          # Biblioteca de SQLite
import sys                              # exit, excepthook, exc_info, ...
from subprocess import call             # Pra executar comandos do S.O.


try:
    # Apaga o arquivo de banco, se existir (o comando é feito verboso)
    call( ['rm', '-frv', 'bancoTeste'] )

    # Sempre começaremos com este banco totalmente vazio, portanto
    con = sqlite3.connect( "bancoTeste" )   # Abre uma conexão
    bd = con.cursor()                       # Prepara para operações
    print( "- Conexão aberta e preparada." )

except:
    print( "- Erro!" )

    # Informações cruas da exceção
    print( sys.exc_info() )

    # Imprime de forma amigável e informativa os dados exceção acontecida
    sys.excepthook( *sys.exc_info() )

    # Termina o programa com um valor de saída que indica erro
    sys.exit( 2 )

dadosDeTeste = \
[
    # inteiro (chave primária)
    # inteiro
    # real
    (
        None,
        13,
        31.13
    )
]

# Insert data
try:
    bd.execute \
    (
        "create table testando \
        ( \
                id	integer not null default 1 unique, \
                mágica	integer, \
                preço	real, \
                primary key(id autoincrement) \
        )"
    )
    print( "- Tabela recriada." )

    bd.executemany \
    (
        "insert into testando values ( ?, ?, ?)",
        dadosDeTeste
    )
    print( "- Dados inseridos." )

    con.commit()
    print( "- Inserção confirmada." )

    con.close()
    print( "- Banco fechado." )

except:
    # Antes de tudo, tenta garantir que o banco fique bem
    con.close()

    print( "- Erro!" )

    # Informações cruas da exceção
    print( sys.exc_info() )

    # Imprime de forma amigável e informativa os dados exceção acontecida
    sys.excepthook( *sys.exc_info() )

    # Termina o programa com um valor de saída que indica erro (retorno di-
    # ferente do erro das exceções possíveis na abertura do banco)
    sys.exit( 3 )

sys.exit( 0 )

# vim: fileencoding=utf-8: expandtab: shiftwidth=4: tabstop=8: softtabstop=4
