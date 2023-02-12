class Pessoa:
    def __init__(self, nome: str, tarefas: list = [], peso_tarefas=0):
        Pessoa.nome = nome  # Nome da pessoa+
        Pessoa.tarefas = tarefas  # Lista de tarefas da pessoa
        Pessoa.peso_tarefas = peso_tarefas  # Somatório dos pesos das tarefas
     
    ''' Atribui uma tarefa a lista de tarefas da pessoa recebendo
    uma variavel da classe tarefa.'''
    
    @tarefas.setter
    def atribuir_tarefa(self, tar):
        Pessoa.tarefas.append(tar)
    

class Tarefa:
    def __init__(self, nome, peso):
        Tarefa.nome = nome  # Nome da tarefa
        Tarefa.peso = peso  # Peso da tarefa


t1 = Tarefa('Lavar Louça', 10)
p1 = Pessoa('Lucas')

p1.atribuir_tarefa(t1)

print(p1.tarefas[0])
