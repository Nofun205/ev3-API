import bcrypt

class Encriptador:
    
    @staticmethod
    def encriptar(password):
        # Generamos una "sal" aleatoria
        salt = bcrypt.gensalt()
        # Encriptamos la contraseña convertida a bytes
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        # Retornamos hash y salt como strings para guardarlos en BD
        return hashed.decode('utf-8'), salt.decode('utf-8')

    @staticmethod
    def validar(password, hashed_password):
        # Comparamos la contraseña ingresada con el hash guardado
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))