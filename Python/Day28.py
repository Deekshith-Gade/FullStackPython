from abc import ABC, abstractmethod
class Vehile(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehile):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stopped")
m=Car()
m.start_engine()
m.stop_engine()

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan_interest(self):
        pass

    def bank_services(self):
        print("Common services: Net Banking, ATM, Mobile App")

class SBI(Bank):
    def loan_interest(self):
        print("SBI interest rate is 8%")

class HDFC(Bank):
    def loan_interest(self):
        print("HDFC interest rate is 10%")


bank1 = SBI()
bank2 = HDFC()

bank1.loan_interest()




