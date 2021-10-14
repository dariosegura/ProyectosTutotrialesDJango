class marca_carro():
    def __init__(self, nombre):
        self.Nombre=nombre
    @staticmethod
    def get_marcas():
        marcas=[
           marca_carro("VolskWagen"),
           marca_carro("BMW"),
           marca_carro("Mercedez Benz"),
           marca_carro("Audi"),
           marca_carro("Lada"),
        ]
        return marcas
