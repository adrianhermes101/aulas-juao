class animal:

    def emitir_som(self):
        return 'Qualquer som'
    
class Cachorro(animal):
    def emitir_som(self):
        return 'auauuauauaua'
    
Cachorro = Cachorro()
print(Cachorro.emitir_som())

class gato(animal):
    def emitir_som(self):
        return 'Miau'