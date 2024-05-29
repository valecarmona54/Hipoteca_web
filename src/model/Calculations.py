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
        Definition:
            Lifetime reverse mortgage: the client collects the annuity until he or she dies. The function returns the calculation

        Returns:
            float: The amount of money to be received periodically in a lifetime reverse mortgage.
    """
    if interest <= 0:
        raise InvalidInterestException(interest)
    
    months = LifeExpectancyCalculation(age, gender) * 12
    monthly_fee = ((total_amount * interest_housing) / months) 
    return monthly_fee + monthly_fee * (interest * months)

def MortgageTemporaryReverse(total_amount, interest, interest_housing, quotas):

    """
        Definition:
            Temporary reverse mortgage: the rent is obtained for a set period of time.
        Returns:
            float: The total amount of money to be received during the established installment period.
    """    
    if interest <= 0:
        raise InvalidInterestException(interest)
    if quotas <= 0 or not isinstance(quotas, int):
        raise InvalidQuotasException(quotas)
    
    monthly_fee = ((total_amount * interest_housing) / quotas) 
    return monthly_fee + monthly_fee * (interest * quotas)

def MortgageSingleReverse(total_amount, interest_housing):

    """
        Definition:
            Single-draw reverse mortgage: The value to be received will be the total sale value of the home.
        Returns:
            float: The total value of the home.
    """
    return total_amount * interest_housing

def LifeExpectancyCalculation(age, gender):
    "Retorna el calculo de la esperanza de vida en base al genero y la edad"
    if age < 65:
        raise InvalidAgeException(age)
    if gender == "M" or gender == "m":
        return 80 - age
    if gender == "F" or gender == "f":
        return 74 - age
    raise ValueError("El género debe ser 'M'/'m' o 'F'/'f'")
