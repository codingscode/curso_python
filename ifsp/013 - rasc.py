# Herança


class Usuario:
    contador = 0

    def __init__(self, nome, email):   # construtor
        self.nome = nome
        self.email = email
        Usuario.contador += 1

    def diga_ola(self):
        print(f'Olá, meu nome é {self.nome} e meu email é {self.email}')


usuario1 = Usuario(nome="Simon", email="simon11@gmail.com")

usuario1.diga_ola()
print(usuario1.nome)

# alterando e acessando propriedades
usuario1.nome = 'Robson'
usuario1.diga_ola()
print(usuario1.nome)

print(f'usuario1 tem propriedade "nome" ?: {hasattr(usuario1, "nome")} ')
print(f'usuario1 tem propriedade "idade" ?: {hasattr(usuario1, "idade")} ')
print(f'acessar valor email de usuario1 : {getattr(usuario1, "email")}')
setattr(usuario1, 'nome', 'Mauricio S.')
setattr(usuario1, 'idade', 23)
print(f'acessar valor nome de usuario1 : {getattr(usuario1, "nome")}')
print(f'acessar idade de usuario1 : {getattr(usuario1, "idade")}')
# delattr(usuario1, 'idade')
print(f'nome : {getattr(usuario1, "nome")}')

print('----------------------')
usuario2 = Usuario(nome="Raul", email="raul2@gmail.com")
print(Usuario.contador)

print('----------------------')


class Administrador(Usuario):
    def __init__(self, nome, email, chave_de_administrador):
        Usuario.__init__(self, nome, email)
        self.chave_de_administrador = chave_de_administrador

    def poder_administrativo(self):
        print(f"Eu tenho o controle! Minha chave é {self.chave_de_administrador}")


usuario_adm = Administrador(nome="Admin", email="admin@admin.com", chave_de_administrador="12345")
usuario_adm.diga_ola()
usuario_adm.poder_administrativo()


print('-------------------------')


class MembroStaff(Usuario):
    def __init__(self, nome, email):
        Usuario.__init__(self, nome, email)

    def diga_ola(self):
        print(f'Olá, meu nome é {self.nome} e sou do Staff.')


membro_staff_1 = MembroStaff(nome='Weber', email='weber@')
membro_staff_1.diga_ola()








