class Std_Name:
    def __init__(self, Std_firstName, Std_Phn, Std_lastName):
        self.Std_firstName = Std_firstName
        self.Std_Phn = Std_Phn
        self.Std_lastName = Std_lastName


Std_firstName = "Wick"
name = Std_Name(Std_firstName, 'F', "Bob")
Std_firstName = "Ann"
name.lastName = "Nick"
print(name.Std_firstName, name.Std_lastName)
