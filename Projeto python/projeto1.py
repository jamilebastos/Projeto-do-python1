lista_tarefa = []

def adicionar_tarefa():
    nome = input(" escreva o nome da tarefa: ")
    prioridade = input ("escreva se é alta, baixa ou média: ")
    categoria = input (" escreva a categoria: ")
    status = input("coloque o status: ")

    tarefa_dicionario = {
         "nome":nome,
         "prioridade":prioridade,
         "categoria": categoria,
         "status": status
    }
   
    lista_tarefa.append(tarefa_dicionario)
    print ("a tarefa foi adicionada")
      

def analisa_tarefa():
     if lista_tarefa:
          for i in range(len(lista_tarefa)):
               print(f"tarefa_dicionario: {i+1}")
               print(f"nome:{lista_tarefa[i]['nome']}")
               print(f"prioridade:{lista_tarefa[i]['prioridade']}")
               print(f"categoria:{lista_tarefa[i]['categoria']}")
               print(f"status:{lista_tarefa[i]['status']}")

     else:
          print("lista vazia, nenhuma tarefa foi achada")

def remover_tarefa():
     nome = input("Qual o nome da tarefa que precisa remover?: ")
     for tarefa_dicionario in lista_tarefa:
          if tarefa_dicionario ["nome"] == nome:
               lista_tarefa.remove(tarefa_dicionario)
               print ("a tarefa foi removida")
               break
          else:
               print("nenhuma tarefa foi encontrado, para remover")
     


while True:
     menu = input ("""
     escolha uma das opções a baixo
     1-adiconar tarefa
     2-ver tarefa
     3-remover tarefa
     4-sair
     """)
     match menu:
          case"1":
               adicionar_tarefa()
          case"2":
               analisa_tarefa()
          case "3":
               remover_tarefa()
          case "4":
               print ("fim do programa")
               break
          case _:
               print("essa opção não existe")



      
   




