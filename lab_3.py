from datetime import datetime

class Bank:

    def __init__(self):
        self.total_amount = 0
        self.name = ''
        self.surname = ''

    def welcome(self):
        self.name, self.surname = input('Welcome to your private bank account! We are happy to see you! '
                                        '\nPlease, enter your name and surname: ').split(' ')
        self.current_time = datetime.now()
        self.stamp = datetime.timestamp(self.current_time)
        self.objectdate = datetime.fromtimestamp(self.stamp)

    def ToString(self):
        print(f'{self.name}, your current balance is: {self.total_amount}')
        print(f'Last entering date: {self.objectdate}')

    def addToBankAccount(self):
        self.total_amount += float(input('{}, please enter amount: '.format(self.name, self.surname)))
        self.ToString()

    def subtractFromBankAccount(self):
        amount_to_withdraw = float(input('Enter amount to withdraw: '))

        if amount_to_withdraw > self.total_amount:
            print('You may not have enough balance !!!')
        else:
            self.total_amount -= amount_to_withdraw

        self.ToString()



if __name__ == "__main__":
    bank = Bank()
    bank.welcome()

while True:
    input_value = int(input('Choose your preferred operation:'
                            '\n1 - Display account information and balance'
                            '\n2 - Add to balance '
                            '\n3 - Subtract from balance '
                            '\n4 - Account information'
                            '\n0 - Exit\n'))
    if input_value == 1:
        bank.ToString()
    elif input_value == 2:
        bank.addToBankAccount()
    elif input_value == 3:
        bank.subtractFromBankAccount()
    elif input_value == 4:
        bank.ToString()
    elif input_value == 0:
            break
    else:
        print('Please enter a valid input.')