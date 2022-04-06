class Lutas:
    def __init__(self, nome_da_luta):
        print(nome_da_luta, 'é um estilo de luta!');


class Arte_Marcial(Lutas):
    def __init__(self, Nome):
        print(Nome, 'é uma arte marcial.')
        super().__init__(Nome)
    

class Não_é_briga(Arte_Marcial):
      def __init__(self, nome):
        print(nome, "não é briga de rua!")
        super().__init__(nome)

class Serve_para_autodefesa(Arte_Marcial):
      def __init__(self, nome):
        print(nome, "serve para autodefesa!")
        super().__init__(nome)


class Não_pode_soco(Arte_Marcial):
    def __init__(self, name):
        print(name, "não pode soco!")
        super().__init__(name)


class Jiu_Jitsu(Não_é_briga, Não_pode_soco):
    def __init__(self):
        print('Jiu Jitsu.');
        super().__init__('Jiu Jitsu')


class Karatê(Não_é_briga, Não_pode_soco, Serve_para_autodefesa):
    def __init__(self):
        print('Karatê.');
        super().__init__('Karatê')      

jiu_jitsu = Jiu_Jitsu()
print('')
muay_thai = Não_é_briga('Muay Thai')
print('')
karate = Karatê()
print('')