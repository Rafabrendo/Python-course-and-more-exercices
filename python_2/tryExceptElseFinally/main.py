try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e: #ZeroDivisionError -> é a uma classe   e -> 'index'
    print(e.__class__.__name__) #vai pegar o nome da classe
    print(e)
    print('DIVIDIU ZERO')

except IndexError as error:
    print('IndexError')

except (NameError, ImportError):
    print('NameError, importError')

else: #vai ser executado caso o código não tenha erros
    print('Não deu erro')

finally: #VAI SER EXECUTADO SEMPRE
    print('FECHAR ARQUIVO')