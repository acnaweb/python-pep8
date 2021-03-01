class filanormal:
    codigo:int=0
    fila=[]
    clientes_atendidos=[]
    senhaatual:str = ""

    def gerasenhaatual(self) -> None:
        self.senhaatual = f"NM{self.codigo}"

    def resetafila(self)->None:
        if self.codigo >= 100:
            self.codigo=0
        else:
            self.codigo+=1

    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa:int)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"cliente atual {cliente_atual}, dirija-se ao {caixa}"
