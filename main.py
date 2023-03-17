class Account:
    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self.name = new_name
        else:
            print("-Error: invalid type.")

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        if isinstance(new_balance, float):
            self.balance = new_balance
        else:
            print("-Error: invalid type.")

    def __str__(self):
        return f"Name: {self.name} - Balance: ${self.balance:.2f}"

class ICA(Account):
    def __init__(self, name="", balance=0, gender="", ssn=""):
        super().__init__(name, balance)
        self.gender = gender
        self.ssn = ssn

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        if isinstance(new_gender, str) and len(new_gender) >= 1:
            self.gender = new_gender
        else:
            print("Invalid input.")

    def get_ssn(self):
        return self.ssn

    def set_ssn(self, new_ssn):
        if isinstance(new_ssn, str) and len(new_ssn) == 9:
            self.ssn = new_ssn
        else:
            print("Invalid input.")

class BCA(Account):
    def __init__(self, name="", balance=0, modality="", ein=""):
        super().__init__(name, balance)
        self.modality = modality
        self.ein = ein

    def get_modality(self):
        return self.modality

    def set_modality(self, new_modality):
        if isinstance(new_modality, str) and len(new_modality) >= 1:
            self.modality = new_modality
        else:
            print("Invalid input.")

    def get_ein(self):
        return self.ein

    def set_ein(self, new_ein):
        if isinstance(new_ein, str) and len(new_ein) == 9:
            self.ein = new_ein
        else:
            print("Invalid input.")

if __name__ == '__main__':
    acc = Account('Alice')
    print(acc)
    print('-Superclass:\nName:', acc.get_name())
    print('Balance:', acc.get_balance())
    acc.set_name('Emily')
    print("Different name:", acc.get_name())
    print(acc.__str__())
    ica1 = ICA('Ana', 3000.0, 'F', '1234')
    print(ica1)
    print(' - ICA 1:\nName:', ica1.get_name())
    print("Balance:", ica1.get_balance())
    ica2 = ICA('Ailton', 7000.0)
    print(ica2)
    print(' - ICA 2:\nName:', ica2.get_name())
    print("Balance:", ica2.get_balance())
    print("SSN:", ica2.get_ssn())
    ica2.set_ssn('123456789')
    print("Different SSN:", ica2.get_ssn())
    print("Output using Python's vars and __dict__ functions:")
    print(vars(ica2))
    print(ica2.__dict__)