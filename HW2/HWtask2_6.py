

'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''


class Bank_account:
    CHECK_OPERATION: int = 50
    TAKE_OF_PERCENT: float = 0.015
    BONUS_PERCENT: float = 0.03
    TAX: float = 0.1
    CRITICAL_VALUE: int = 5000000
    OPERATION: int = 0
    balance: int = 0

    def __init__(self):
        self.OPERATION = 0

    def deposit_account(self, deposit_value: int, tax: int) -> tuple[int, int] | None:
        if deposit_value % self.CHECK_OPERATION == 0:
            self.balance += deposit_value + tax
            self.OPERATION += 1
            return self.balance, self.OPERATION
        else:
            return None

    def take_money_from_account(self, take_money: int, tax: int, commision: int) -> tuple[int, int] | None:
        if take_money % self.CHECK_OPERATION == 0 and self.balance > 0 and self.balance - (
                take_money + commision + tax) >= 0:
            self.balance -= take_money + commision + tax
            self.OPERATION += 1
            return self.balance, self.OPERATION
        else:
            return None

    def calculate_commision(self, money_value: int) -> int:
        MIN_COMMISION: int = 30
        MAX_COMMISION: int = 600
        sum_commision: int = money_value * self.TAKE_OF_PERCENT

        if sum_commision > MAX_COMMISION:
            sum_commision = MAX_COMMISION
        elif sum_commision < MIN_COMMISION:
            sum_commision = MIN_COMMISION
        else:
            sum_commision = int(sum_commision)
        return sum_commision

    def calculate_tax(self, money_value: int) -> int:
        if money_value >= self.CRITICAL_VALUE:
            tax_value = money_value * self.TAX
            print(f"Снятие налога на богатсво в размере --> {tax_value}")
            return tax_value
        else:
            return 0

    def exit_from_ATM(self) -> str:
        res = "Выход"
        return res

    def add_bonus(self):
        self.balance += self.balance * self.BONUS_PERCENT
        return f"Были зачислены бонусы в размере {int(self.balance * self.BONUS_PERCENT)} за выполнение трех операций"

    def start(self, action: str, money_value: int) -> str:
        if self.OPERATION % 3 == 0 and self.OPERATION != 0:
            print(self.add_bonus())
        tax = self.calculate_tax(money_value)
        match action:
            case "Пополнить":
                self.deposit_account(money_value, tax)
                return f"Зачислено: {money_value}, баланс: {int(self.balance)}"
            case "Снять":
                commision = self.calculate_commision(money_value)
                data = self.take_money_from_account(money_value, commision, tax)
                if data:
                    return f"Со счета снято {money_value}, коммисия составил: {commision}, баланс: {int(self.balance)}"
                else:
                    return "Недостаточно средств"
            case "Выход":
                return self.exit_from_ATM()


bank = Bank_account()
print(bank.start(action="Пополнить", money_value=1500000))
print(bank.start(action="Пополнить", money_value=4600000))
print(bank.start(action="Снять", money_value=100000))
print(bank.start(action="Пополнить", money_value=100000))
print(bank.start(action="Пополнить", money_value=1100000))
print(bank.start(action="Пополнить", money_value=2000050))
print(bank.start(action="Снять", money_value=5000000))
print(bank.start(action="Выход", money_value=0))
