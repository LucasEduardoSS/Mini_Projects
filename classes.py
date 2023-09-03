# Retorna o modulo de um número
def modulo(x):
    return (x**2)**0.5


# Valida uma entrada do tipo inteiro
def int_input():
    while True:
        try:
            var = int(input("Digite aqui:"))
            return var
        except ValueError:
            print("\33[31mValor inválido, tente novamente!\33[m")


# Imprime um titulo
def titulo(mgs, tam):
    print("-" * tam), print(f"{mgs:^{tam}}"), print("-" * tam)


# Imprime as tabelas de registros
def tabela_registros(tbl_pessoas: list, tbl_registros: list, tipo, subtitulo=False):
    # Imprime a tabela de registro de pessoas
    if tipo == "P":
        titulo("Pessoas Registradas", 50)
        if subtitulo:
            print(f'{"Cód":<5}{"Nome":<45}')
        for pos, p in enumerate(tbl_pessoas):
            print(f'{pos:<5}{p["Nome"]:<45}')
        print("-" * 50)

    # Imprime a tabela de registro de tarefas
    elif tipo == "T":
        titulo("Tarefas Registradas", 50)
        if subtitulo:
            print(f'{"Cód":<5}{"Nome":<40}{"Peso":<5}')
        for pos, t in enumerate(tbl_registros):
            print(f'{pos:<5}{t["Nome"]:<40}{t["Peso"]:<5}')
        print("-" * 50)
