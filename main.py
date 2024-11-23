class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.quartos = []
        self.reservas = []
        self.id_cliente = 1
        self.id_quarto = 1

    def cadastrar_cliente(self):
        print("\nCadastrar Cliente")
        nome = input("Digite o nome do cliente: ")
        idade = input("Digite a idade do cliente: ")
        documento = input("Digite o documento do cliente (RG ou CPF): ")

        # Verificação de dados
        if not nome or not idade.isdigit() or not documento:
            print("Erro: Dados inválidos!")
            return

        cliente = {'id': self.id_cliente, 'nome': nome, 'idade': idade, 'documento': documento}
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        self.id_cliente += 1

    def ver_clientes(self):
        print("\nClientes Cadastrados:")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Idade: {cliente['idade']}, Documento: {cliente['documento']}")

    def editar_cliente(self):
        print("\nEditar Cliente")
        try:
            id_cliente = int(input("Digite o ID do cliente a ser editado: "))
            cliente_encontrado = False
            for cliente in self.clientes:
                if cliente['id'] == id_cliente:
                    novo_nome = input("Digite o novo nome: ")
                    nova_idade = input("Digite a nova idade: ")
                    novo_documento = input("Digite o novo documento: ")

                    # Verificação de dados
                    if not novo_nome or not nova_idade.isdigit() or not novo_documento:
                        print("Erro: Dados inválidos!")
                        return

                    cliente['nome'] = novo_nome
                    cliente['idade'] = nova_idade
                    cliente['documento'] = novo_documento
                    print(f"Cliente {novo_nome} atualizado com sucesso!")
                    cliente_encontrado = True
                    break
            if not cliente_encontrado:
                print("Erro: Cliente não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    def remover_cliente(self):
        print("\nRemover Cliente")
        try:
            id_cliente = int(input("Digite o ID do cliente a ser removido: "))
            cliente_encontrado = False
            for cliente in self.clientes:
                if cliente['id'] == id_cliente:
                    self.clientes.remove(cliente)
                    print(f"Cliente {cliente['nome']} removido com sucesso!")
                    cliente_encontrado = True
                    break
            if not cliente_encontrado:
                print("Erro: Cliente não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    def cadastrar_quarto(self):
        print("\nCadastrar Quarto")
        try:
            numero = input("Digite o número do quarto: ")
            tipo = input("Digite o tipo de quarto (Ex: Simples, Duplo, Luxo): ")
            preco = input("Digite o preço do quarto: ")

            # Verificação de dados
            if not numero.isdigit() or not tipo or not preco.replace('.', '', 1).isdigit():
                print("Erro: Dados inválidos!")
                return

            quarto = {'id': self.id_quarto, 'numero': numero, 'tipo': tipo, 'preco': preco}
            self.quartos.append(quarto)
            print(f"Quarto {numero} cadastrado com sucesso!")
            self.id_quarto += 1
        except ValueError:
            print("Erro: Dados inválidos!")

    def ver_quartos(self):
        print("\nQuartos Cadastrados:")
        if not self.quartos:
            print("Nenhum quarto cadastrado.")
        else:
            for quarto in self.quartos:
                print(f"ID: {quarto['id']}, Número: {quarto['numero']}, Tipo: {quarto['tipo']}, Preço: {quarto['preco']}")

    def editar_quarto(self):
        print("\nEditar Quarto")
        try:
            id_quarto = int(input("Digite o ID do quarto a ser editado: "))
            quarto_encontrado = False
            for quarto in self.quartos:
                if quarto['id'] == id_quarto:
                    novo_tipo = input("Digite o novo tipo de quarto: ")
                    novo_preco = input("Digite o novo preço: ")

                    # Verificação de dados
                    if not novo_tipo or not novo_preco.replace('.', '', 1).isdigit():
                        print("Erro: Dados inválidos!")
                        return

                    quarto['tipo'] = novo_tipo
                    quarto['preco'] = novo_preco
                    print(f"Quarto {id_quarto} atualizado com sucesso!")
                    quarto_encontrado = True
                    break
            if not quarto_encontrado:
                print("Erro: Quarto não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    def remover_quarto(self):
        print("\nRemover Quarto")
        try:
            id_quarto = int(input("Digite o ID do quarto a ser removido: "))
            quarto_encontrado = False
            for quarto in self.quartos:
                if quarto['id'] == id_quarto:
                    self.quartos.remove(quarto)
                    print(f"Quarto {quarto['numero']} removido com sucesso!")
                    quarto_encontrado = True
                    break
            if not quarto_encontrado:
                print("Erro: Quarto não encontrado.")
        except ValueError:
            print("Erro: ID inválido.")

    def fazer_reserva(self):
        print("\nFazer Reserva")
        nome_cliente = input("Digite o nome do cliente para realizar a reserva: ")
        numero_quarto = input("Digite o número do quarto para reserva: ")
        data_reserva = input("Digite a data da reserva (DD/MM/AAAA): ")

        # Verificação de dados
        if not data_reserva:
            print("Erro: Data inválida!")
            return

        cliente_encontrado = False
        quarto_encontrado = False

        for cliente in self.clientes:
            if cliente['nome'] == nome_cliente:
                cliente_encontrado = True
                break

        for quarto in self.quartos:
            if quarto['numero'] == numero_quarto:
                quarto_encontrado = True
                break

        if cliente_encontrado and quarto_encontrado:
            reserva = {'cliente': nome_cliente, 'quarto': numero_quarto, 'data': data_reserva}
            self.reservas.append(reserva)
            print(f"Reserva para {nome_cliente} no quarto {numero_quarto} realizada com sucesso!")
        else:
            if not cliente_encontrado:
                print("Erro: Cliente não encontrado.")
            if not quarto_encontrado:
                print("Erro: Quarto não encontrado.")

    def encerrar_reserva(self):
        print("\nEncerrar Reserva")
        nome_cliente = input("Digite o nome do cliente para encerrar a reserva: ")
        numero_quarto = input("Digite o número do quarto para encerrar a reserva: ")

        reserva_encontrada = False
        for reserva in self.reservas:
            if reserva['cliente'] == nome_cliente and reserva['quarto'] == numero_quarto:
                self.reservas.remove(reserva)
                print(f"Reserva de {nome_cliente} no quarto {numero_quarto} encerrada com sucesso!")
                reserva_encontrada = True
                break

        if not reserva_encontrada:
            print("Erro: Reserva não encontrada.")

    def ver_quartos_reservados(self):
        print("\nQuartos Reservados:")
        if not self.reservas:
            print("Nenhuma reserva realizada.")
        else:
            for reserva in self.reservas:
                print(f"Cliente: {reserva['cliente']}, Quarto: {reserva['quarto']}, Data: {reserva['data']}")

    def ver_quartos_disponiveis(self):
        print("\nQuartos Disponíveis:")
        quartos_reservados = [reserva['quarto'] for reserva in self.reservas]
        disponiveis = [quarto for quarto in self.quartos if quarto['numero'] not in quartos_reservados]

        if not disponiveis:
            print("Nenhum quarto disponível.")
        else:
            for quarto in disponiveis:
                print(f"Número: {quarto['numero']}, Tipo: {quarto['tipo']}, Preço: {quarto['preco']}")

def menu(hotel):
    while True:
        print("\n---- Menu Principal ----")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Quartos")
        print("3. Gerenciar Reservas")
        print("0. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                menu_clientes(hotel)
            elif opcao == 2:
                menu_quartos(hotel)
            elif opcao == 3:
                menu_reservas(hotel)
            elif opcao == 0:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Digite um número válido.")

def menu_clientes(hotel):
    while True:
        print("\n---- Gerenciar Clientes ----")
        print("1. Cadastrar Cliente")
        print("2. Ver Clientes")
        print("3. Editar Cliente")
        print("4. Remover Cliente")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                hotel.cadastrar_cliente()
            elif opcao == 2:
                hotel.ver_clientes()
            elif opcao == 3:
                hotel.editar_cliente()
            elif opcao == 4:
                hotel.remover_cliente()
            elif opcao == 0:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Digite um número válido.")

def menu_quartos(hotel):
    while True:
        print("\n---- Gerenciar Quartos ----")
        print("1. Cadastrar Quarto")
        print("2. Ver Quartos")
        print("3. Editar Quarto")
        print("4. Remover Quarto")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                hotel.cadastrar_quarto()
            elif opcao == 2:
                hotel.ver_quartos()
            elif opcao == 3:
                hotel.editar_quarto()
            elif opcao == 4:
                hotel.remover_quarto()
            elif opcao == 0:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Digite um número válido.")

def menu_reservas(hotel):
    while True:
        print("\n---- Gerenciar Reservas ----")
        print("1. Fazer Reserva")
        print("2. Ver Quartos Reservados")
        print("3. Ver Quartos Disponíveis")
        print("4. Encerrar Reserva")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                hotel.fazer_reserva()
            elif opcao == 2:
                hotel.ver_quartos_reservados()
            elif opcao == 3:
                hotel.ver_quartos_disponiveis()
            elif opcao == 4:
                hotel.encerrar_reserva()
            elif opcao == 0:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Digite um número válido.")

# Exemplo de uso:
hotel = Hotel("Hotel Teste")
menu(hotel)
