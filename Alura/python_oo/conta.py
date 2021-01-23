class Conta:
    def __init__ (self, titular, saldo=0, agencia="0000-0"):
        self._conta = {"titular": titular, "saldo": saldo, "agencia":agencia}
    
    @property  
    def saldo(self):
        return self._conta["saldo"]

    @saldo.setter
    def saldo(self, novo_saldo):
        self._conta["saldo"] = novo_saldo
        return self._conta["saldo"]

    @property
    def agencia(self):
        return self._conta["agencia"]
    
    @agencia.setter
    def agencia(self, nova_agencia):
        self._conta["agencia"] = nova_agencia
        return self._conta["agencia"]


        

