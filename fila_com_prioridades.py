import os

class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Paciente:
    def __init__(self):
        os.system("cls")
        self.lista_pacientes = []
        self.prioridade = ()
        self.dados_paciente = ()
        self.contador = 999
        self.max_heap = MaxHeap()
        self.lista = []
        self.pacientes_chamados = []
   
    def _add_paciente(self, prioridade, nome_completo, tipo_sanguineo, data_nascimento):
        self.prioridade = prioridade
        self.dados_paciente = self.prioridade, self.contador, nome_completo, tipo_sanguineo, data_nascimento
        self.lista_pacientes.append(self.dados_paciente)
        self.max_heap.put(self.prioridade)
        self.contador -= 1
        print("\nPaciente Adicionado!\n\n")

    def _mostrar_proximo_paciente(self):
        if not self.lista_pacientes:
            print("Não há um próximo Paciente!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.lista_pacientes[i][0] == self.lista[0]:
                        print(f"Próximo Paciente: {self.lista_pacientes[i]}")
                        break  
                elif len(self.lista_pacientes) == 1:
                        print(self.lista_pacientes[0])
                        break
                else:
                        i += 1

    def _chamar_proximo_paciente(self):
        if not self.lista_pacientes:
            print("Não há nenhum Paciente para chamar!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.lista_pacientes[i][0] == self.lista[0]:
                        print(f"Paciente Chamado: {self.lista_pacientes[i]}")
                        self.pacientes_chamados.append(self.lista_pacientes[i])
                        self.lista.pop(0)
                        self.lista_pacientes[i], self.lista_pacientes[0] = self.lista_pacientes[0], self.lista_pacientes[i]
                        self.lista_pacientes.pop(0)
                        break
                else:
                        i += 1
        
    def _mostrar_5_ultimos_pacientes(self):
        if len(self.lista_pacientes) < 5:
            print(f"Último(s) Paciente(s) Chamado(s): {self.pacientes_chamados}")
        else:
            print(f"Últimos 5 Pacientes Chamados: {self.pacientes_chamados[-5]}")

#------------------------------------------------ Menu ------------------------------------------------

p = Paciente()

while True:    
    print("\n1- Adicionar Paciente\n2- Chamar próximo Paciente\n3- Mostrar próximo Paciente\n4- Mostrar 5 últimos Pacientes chamados\n5- Sair")

    escolha = int(input("\n\nO que deseja fazer? "))
    os.system("cls")

    if escolha == 1:
        nome_completo = str(input("\nInforme o nome completo do paciente: "))
        
        prioridade = int(input("Informe a prioridade: ")) 
        while prioridade < 1 or prioridade > 10:
            print("Prioridade Inválida!\n")
            prioridade = int(input("Informe a prioridade: "))
        
        tipo_sanguineo = str(input("Informe o tipo sanguíneo do paciente: ")) 
        data_nascimento = str(input("Informe a data de nascimento do paciente: "))
        p._add_paciente(prioridade, nome_completo, tipo_sanguineo, data_nascimento)
    elif escolha == 2:
        p._chamar_proximo_paciente()
    elif escolha == 3:
        p._mostrar_proximo_paciente()
    elif escolha == 4:
        p._mostrar_5_ultimos_pacientes()
    elif escolha == 5:
        break
    else:
        print("Opção inválida!")
