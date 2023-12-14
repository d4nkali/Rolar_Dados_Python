# Rolar dados RPG por d4nkali 

# Importa as bibliotecas
import tkinter as tk
import random


############################################################################################


# Função para lançar um D2 (Moeda)
def lancar_d2():
    return random.randint(1, 2)

# Função para lançar um D3
def lancar_d3():
    return random.randint(1, 3)

# Função para lançar um D4
def lancar_d4():
    return random.randint(1, 4)

# Função para lançar um D6
def lancar_d6():
    return random.randint(1, 6)

# Função para lançar um D8
def lancar_d8():
    return random.randint(1, 8)

# Função para lançar um D10
def lancar_d10():
    return random.randint(0, 9)

# Função para lançar um D12
def lancar_d12():
    return random.randint(1, 12)

# Função para lançar um D20
def lancar_d20():
    return random.randint(1, 20)


############################################################################################


# Função a ser chamada quando o botão do D2 (Moeda) for clicado
def acao_d2():
    resultado = lancar_d2()
    label_resultado.config(text=f"Resultado do dado de 2 faces ou Moeda: {resultado}")

# Função a ser chamada quando o botão do D3 for clicado
def acao_d3():
    resultado = lancar_d3()
    label_resultado.config(text=f"Resultado do dado de 3 faces: {resultado}")

# Função a ser chamada quando o botão do D4 for clicado
def acao_d4():
    resultado = lancar_d4()
    label_resultado.config(text=f"Resultado do dado de 4 faces: {resultado}")

# Função a ser chamada quando o botão do D6 for clicado
def acao_d6():
    resultado = lancar_d6()
    label_resultado.config(text=f"Resultado do dado de 6 faces: {resultado}")

# Função a ser chamada quando o botão do D8 for clicado
def acao_d8():
    resultado = lancar_d8()
    label_resultado.config(text=f"Resultado do dado de 8 faces: {resultado}")

# Função a ser chamada quando o botão do D10 for clicado
def acao_d10():
    resultado = lancar_d10()
    label_resultado.config(text=f"Resultado do dado de 10 faces: {resultado}")

# Função a ser chamada quando o botão do D12 for clicado
def acao_d12():
    resultado = lancar_d12()
    label_resultado.config(text=f"Resultado do dado de 12 faces: {resultado}")

# Função a ser chamada quando o botão do D20 for clicado
def acao_d20():
    resultado = lancar_d20()
    label_resultado.config(text=f"Resultado do dado de 20 faces: {resultado}")


############################################################################################


# Criar a janela principal
janela = tk.Tk()
janela.title("Dados RPG")

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()


############################################################################################


# Botão para lançar o dado de 2 faces/Moeda
botao_d2 = tk.Button(janela, text="Lançar Moeda", command=acao_d2)
botao_d2.pack()

# Botão para lançar o dado de 3 faces
botao_d3 = tk.Button(janela, text="Lançar D3", command=acao_d3)
botao_d3.pack()

# Botão para lançar o dado de 4 faces
botao_d4 = tk.Button(janela, text="Lançar D4", command=acao_d4)
botao_d4.pack()

# Botão para lançar o dado de 6 faces
botao_d6 = tk.Button(janela, text="Lançar D6", command=acao_d6)
botao_d6.pack()

# Botão para lançar o dado de 8 faces
botao_d8 = tk.Button(janela, text="Lançar D8", command=acao_d8)
botao_d8.pack()

# Botão para lançar o dado de 10 faces
botao_d10 = tk.Button(janela, text="Lançar D10", command=acao_d10)
botao_d10.pack()

# Botão para lançar o dado de 12 faces
botao_d12 = tk.Button(janela, text="Lançar D12", command=acao_d12)
botao_d12.pack()

# Botão para lançar o dado de 20 faces
botao_d20 = tk.Button(janela, text="Lançar D20", command=acao_d20)
botao_d20.pack()


############################################################################################


# Iniciar a interface gráfica
janela.mainloop()
