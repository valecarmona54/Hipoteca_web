class InvalidAgeException(Exception):
    def __init__(self, age, message="La edad debe ser 65 o mayor"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InvalidInterestException(Exception):
    def __init__(self, interest, message="El interés debe ser un número positivo"):
        self.interest = interest
        self.message = message
        super().__init__(self.message)

class InvalidQuotasException(Exception):
    def __init__(self, quotas, message="El número de cuotas debe ser un número entero positivo"):
        self.quotas = quotas
        self.message = message
        super().__init__(self.message)

def MortgageLifetimeInverse(total_amount, interest, interest_housing, age, gender):
    """
    Definición:
        Hipoteca inversa vitalicia: el cliente recibe una anualidad hasta su fallecimiento. La función devuelve el cálculo.
    
    Parámetros:
        total_amount (float): Valor total de la propiedad.
        interest (float): Tasa de interés anual.
        interest_housing (float): Tasa de interés relacionada con la vivienda.
        age (int): Edad del solicitante.
        gender (str): Género del solicitante ('M' para masculino, 'F' para femenino).
    
    Retorna:
        float: Cantidad de dinero a recibir periódicamente en una hipoteca inversa vitalicia.
    
    Excepciones:
        InvalidInterestException: Si el interés no es un número positivo.
    """
    if interest <= 0:
        raise InvalidInterestException(interest)
    
    # Calcula el número de meses basado en la esperanza de vida
    months = LifeExpectancyCalculation(age, gender) * 12
    
    # Calcula la cuota mensual
    monthly_fee = (total_amount * interest_housing) / months
    
    # Devuelve la cuota mensual ajustada por el interés
    return monthly_fee + monthly_fee * (interest * months)

def MortgageTemporaryReverse(total_amount, interest, interest_housing, quotas):
    """
    Definición:
        Hipoteca inversa temporal: la renta se obtiene por un período de tiempo determinado.
    
    Parámetros:
        total_amount (float): Valor total de la propiedad.
        interest (float): Tasa de interés anual.
        interest_housing (float): Tasa de interés relacionada con la vivienda.
        quotas (int): Número de cuotas (mensuales).
    
    Retorna:
        float: Cantidad total de dinero a recibir durante el período de cuotas establecido.
    
    Excepciones:
        InvalidInterestException: Si el interés no es un número positivo.
        InvalidQuotasException: Si el número de cuotas no es un número entero positivo.
    """
    if interest <= 0:
        raise InvalidInterestException(interest)
    if quotas <= 0 or not isinstance(quotas, int):
        raise InvalidQuotasException(quotas)
    
    # Calcula la cuota mensual
    monthly_fee = (total_amount * interest_housing) / quotas
    
    # Devuelve la cuota mensual ajustada por el interés
    return monthly_fee + monthly_fee * (interest * quotas)

def MortgageSingleReverse(total_amount, interest_housing):
    """
    Definición:
        Hipoteca inversa de pago único: el valor a recibir será el valor total de venta de la vivienda.
    
    Parámetros:
        total_amount (float): Valor total de la propiedad.
        interest_housing (float): Tasa de interés relacionada con la vivienda.
    
    Retorna:
        float: Valor total de la propiedad.
    """
    return total_amount * interest_housing

def LifeExpectancyCalculation(age, gender):
    """
    Retorna el cálculo de la esperanza de vida en base al género y la edad.
    
    Parámetros:
        age (int): Edad del solicitante.
        gender (str): Género del solicitante ('M' para masculino, 'F' para femenino).
    
    Retorna:
        int: Número de años restantes esperados de vida.
    
    Excepciones:
        InvalidAgeException: Si la edad es menor de 65 años.
        ValueError: Si el género no es 'M'/'m' o 'F'/'f'.
    """
    if age < 65:
        raise InvalidAgeException(age)
    if gender in ["M", "m"]:
        return 80 - age
    if gender in ["F", "f"]:
        return 74 - age
    raise ValueError("El género debe ser 'M'/'m' o 'F'/'f'")
