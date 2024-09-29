# definição de funções.

def relacao_imc (imc):
    if(imc <= 16.9):
        return 'Muito abaixo do peso.'
    elif (imc > 16.9 and imc <= 18.4):
        return 'Abaixo do peso.'
    elif (imc > 18.4 and imc <= 24.9):
        return 'Peso normal.'
    elif (imc > 24.9 and imc <= 29.9):
        return 'Acima do peso.'        
    elif (imc > 29.9 and imc <= 34.9):
        return 'Obesidade grau I.'
    elif (imc > 34.9 and imc <= 40):
        return 'Obesidade grau II.'   
    elif imc > 40:
        return 'Obesidade grau III.'

def formulario_imc():
    dados = []
    altura = float(input("Sua altura em metros: "))
    massa = float(input("Sua massa em kilogramas: "))

    print('------------------------------------------------')
    print(f"Valores informados:\n")
    print(f"Altura: {altura} m")
    print(f"Massa: {massa} kg")
    print('------------------------------------------------')

    dados.append(altura)
    dados.append(massa)

    return dados

# início da interação com o usuário.

print("Boas-vindas ao aplicativo Minha Massa.")
print("Calcule seu IMC agora.\n")

name = input("Insira seu nome: ").capitalize()
print(f"\nOlá, {name}. Vamos calcular o seu IMC. Informe os seguintes dados:")

#loop que permite alteração das informações pelo usuário em caso de preenchimento errôneo de algum dos dados..

while True:
    resultado = formulario_imc()

    is_correct = input("Estão corretos? (S para SIM / N para NÃO) ").upper()

    if is_correct == 'S':
        imc = resultado[1] / (resultado[0] ** 2)
        print(f"\n{name}, seu IMC atual é: {imc:.2f} e está dentro da classificação: {relacao_imc(imc)}")
        break
        
    else:
        print(f"\nSem problemas, {name}. Vamos tentar novamente...")
        print("Informe os seguintes dados:\n")


