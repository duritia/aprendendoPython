Como imprimir informações úteis para exceções que aconteçam nos programas
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Não foi ensinado. Não pareceu que existiria. Foi uma coisa mencionada na discussão¹ que fiz sobre inserções mal sucedidas em SQLite. Mas não foi uma coisa óbvia de achar! Então, fiz este programete pra não esquecer dela, e esta documentação que o acompanha para quaisquer esclarecimentos que alguém ache necessário.

A mensagem chave que fiz na discussão onde descobri "o segredo": https://www.linuxquestions.org/questions/programming-9/python-executes-without-errors-or-warnings-but-data-is-not-inserted-in-sqlite-database-4175713940/#post6365204

Explicação: quando acontece uma exceção em um bloco **try**, ela guarda informações sobre o que aconteceu. Tais informações podem ser recuperadas e processadas no respectivo block **except**, para mostrar uma mensagem de erro amigável e informativa.

O programete dado é um pequeno exemplo disto.

# vim: fileencoding=utf-8: expandtab: shiftwidth=4: tabstop=8: softtabstop=4
