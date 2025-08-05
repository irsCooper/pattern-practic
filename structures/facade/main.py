from services import Builder, Investor, Vendor

"""
Фасад -- структурный паттерн, предоставлояющий простой (но урезанный) интерфейс к сложной системе объектов

Позволяет снизить общую сложность программы и помогает вынести код, зависимый от внешней системы в отдельное место

Когда применять:
- клиентское приложение для работы со сложными api
"""


class Facade:
    def __init__(self):
        self.investor: Investor = Investor()
        self.vendor: Vendor = Vendor()
        self.builder: Builder = Builder()

    def start_project(self):
        for i in range(3):
            self.investor.investing()
        
        for i in range(10):
            self.vendor.give()
        
        for i in range(50):
            self.builder.build()

        print("Project finished!")

if __name__ == "__main__":
    facade: Facade = Facade()
    facade.start_project()