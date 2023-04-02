class Own_Exeptions(Exception):
    def __init__(self, numero_error):
        self.numero_error = numero_error
        super().__init__(self.numero_error)

    def __str__(self):
        return f'{self.numero_error}'
    
    def error_not_found(self):
        if self.numero_error == 404:
            return f"Error {self.numero_error}: El anime no se encuentra en la lista"
