lista_de_produtos = ["000a","000b", "000c", "000d", "0001", "0002", "0003","0004", "0005"]
lista_de_materiais =  ["plastico", "metal", "plastico", "papel", "vidro", "vidro", "papel", "metal", "plastico"]

plasticos = 0
metais = 0
papeis = 0
vidros = 0
saldo = 0

def validar_opcao(lista, frase):
    opcao = input(frase)
    while opcao not in lista:
        print("Digite uma opção válida.")
        opcao = input(frase)
    return opcao

def cadastrar_produto(codigo, composicao):
    lista_de_produtos.append(codigo)
    lista_de_materiais.append(composicao)
    return

def consultar_produto(codigo_do_produto):
    if codigo_do_produto in lista_de_produtos:
        return "Esse produto já está cadastrado na nossa base!"
    elif len(codigo_do_produto) != 4:
        return "Esse código não é válido. Tente novamente."
    else:
        print("Esse produto ainda não está cadastrado no nosso sistema. ")
        opcao = validar_opcao(["plastico", "metal", "vidro", "papel"], "Digite a composição do produto (plastico, metal, vidro, papel):  ")
        cadastrar_produto(codigo_do_produto, opcao)
        return "Agora sim, o produto já foi cadastrado e pode ser descartado em nossa máquina!"

def depositar_residuo(residuo):
    global papeis, vidros, metais, plasticos, saldo

    if residuo not in lista_de_produtos:
        return '''\nOps! Não encontramos esse produto na nossa base. 
Verifique se o código foi digitado corretamente, com 4 dígitos. Se sim, acesse a opção [2] para consultá-lo e tente novamente. '''
    else:
        for i in range(len(lista_de_produtos)):
            if residuo == lista_de_produtos[i]:
                material = lista_de_materiais[i]
        if material == 'plastico':
            plasticos += 1
        elif material == 'metal':
            metais += 1
        elif material == 'papel':
            papeis += 1
        else:
            vidros += 1
        saldo += 25
        return f"Produto de {material} depositado com sucesso!"

def conhecer_lixeira():
    print('''    Você já imaginou poder ajudar o meio ambiente e ainda ser recompensado por isso? Pois agora isso é 
    possível com a EcoSort! Para usá-la, é muito simples: basta aproximar o código de barras de uma embalagem cadastrada 
    em nossa base e depositá-la que ela já será reciclada. E o melhor: você ganha prêmios por fazer sua parte!

    A EcoSort é capaz de reconhecer qual material foi depositado para separá-lo e garantir que sejam descartados corretamente. 
    Além disso, com o nosso sistema de recompensas, você acumulará pontos que poderão ser trocados por recompensas de nossos 
    parceiros de acordo com a quantidade de itens depositados. Ou seja, quanto mais itens reciclar, mais créditos receberá
    e mais recompensas poderá trocar!
    
    Além disso, caso uma embalagem não esteja registrada no nosso sistema, basta cadastrá-la em nosso site para que nosso
    time faça a validação e cadastre-a na base de dados. Dessa forma, todas as embalagens poderão ser descartadas por aqui.
    Não é demais? 

    E não para por aí! Com a lixeira inteligente, você ainda contribui para a construção de um futuro mais sustentável e
    ajuda a preservar o meio ambiente para as próximas gerações. Então, o que está esperando? Faça parte desse movimento 
    pela reciclagem e comece a ser recompensado por suas ações conscientes! ''')

    return

print("Seja bem vindo à EcoSort - A Lixeira Inteligente da EcoSpark")

while True:
    atividade = validar_opcao(["1", "2", "3", "4", "5"], '''\nO que você quer fazer?
[1] Depositar um resíduo na lixeira
[2] Consultar ou cadastrar um produto
[3] Consultar seu saldo
[4] Conhecer nossa lixeira
[5] Encerrar sua sessão\n''')

    if atividade == "1":
        produto = input("\nDigite o código de barras do produto a ser descartado: ")
        print(depositar_residuo(produto))

    elif atividade == "2":
        produto = input("\nDigite o código de barras do produto para que possamos fazer a consulta: ")
        print(consultar_produto(produto))
    elif atividade == "3":
        print(f"\nO seu saldo acumulado é de {saldo} pontos. Você pode trocar seus pontos por recompensas através do nosso site! ")
    elif atividade == "4":
        conhecer_lixeira()
    else:
        if (vidros or metais or papeis or plasticos) != 0:
            print(f'''Você depositou:
{vidros} embalagens de vidro
{metais} embalagens de metal
{papeis} embalagens de papel
{plasticos} embalagens de plástico
\nE contribuiu com o descarte correto de resíduos e a preservação do meio ambiente!''')
        print("Obrigado por conhecer a EcoSort!")
        break
