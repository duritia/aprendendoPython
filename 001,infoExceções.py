"""
Como imprimir informações úteis para exceções que aconteçam nos programas
"""
import sys

try:
    print( "oi" )
    sys.exit( 0 )
except:
    print( "erro:" )

    # Imprime de forma "crua" a saída da função exc_info()
    print( sys.exc_info() )

    # Imprime de forma amigável e informativa os dados exceção acontecida
    sys.excepthook( *sys.exc_info() )

    sys.exit( 1 )

# Estas duas linhas nunca serão executadas:
print( 'fim' )
sys.exit( 0 )

# Ver: https://www.linuxquestions.org/questions/programming-9/python-executes-without-errors-or-warnings-but-data-is-not-inserted-in-sqlite-database-4175713940/#post6365204

# vim: fileencoding=utf-8: expandtab: shiftwidth=4: tabstop=8: softtabstop=4
