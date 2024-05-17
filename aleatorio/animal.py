class animal():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''
    sexo = 'Macho'


class Cachorro(animal):
    tem_pelo = True
    especie = 'Canis lupus familiaris'
    raça = 'Shitzu'
    nome = 'Sergio'
    porte = 'pequeno'


    def latir():
        return 'AUAUAUAUAUAUAUAUAUA'
    
    def comer():
        return 'caraio'
    
    def dormir():
        return 'ZZZZZZZZZZ'
    
print(Cachorro.comer())
print(Cachorro.dormir())
print(Cachorro.latir())
print(Cachorro.especie)
print(Cachorro.nome)
print(Cachorro.quantidade_patas)
print(Cachorro.porte)
print(Cachorro.raça)
print(Cachorro.sexo)
print(Cachorro.tem_pelo)
print(Cachorro.tem_rabo)