import re

class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = self._validate_phone_number(phone_number)
    
    def _validate_phone_number(self, number):
        if not isinstance(number, str):
            raise ValueError("Номер телефона должен быть строкой")
        
        cleaned = re.sub(r'[\s-]', '', number)
        
        if not re.fullmatch(r'\+79\d{9}', cleaned):
            raise ValueError(
                "Номер телефона должен быть в формате +79XXXXXXXXX "
                "(11 цифр, начинается с +79)"
            )
        return cleaned
    
    def __str__(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"
