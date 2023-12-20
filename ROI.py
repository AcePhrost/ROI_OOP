class Roi_calc():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.investment = 0

    def get_income(self):
        rent = input('how much rent do you collect?')
        laundry = input('How much income do you generate with laundry?')
        parking = input('How much parking do you collect?')
        others = input('What are the other fees you collect?')
        # as many of these as you need to get to a total
        self.income = rent + laundry + parking
        print(f'Cool your income is {self.income}')

    def get_expenses(self):
        tax = input('what are your prop taxes?')
        utilites = input('How much do you pay in utilites?')
        HOA = input('How much are you\'re HOA fees?')
        property_mang = input('How much is property management?')

        self.expenses = tax + utilites + HOA + property_mang

        # finish
    def get_investment(self):
        self.get_income()
        self.get_expenses()
        total_invest = self.get_expenses - self.get_income
        print(f'You\'re total investment is {total_invest}')
        


    def runner(self):
        while True:
            menu = input('1-enter income, 2-enter expenses, 3- enter investment, q to quit\t')
            if menu == '1':
                self.get_income()
            elif menu == '2':
                self.get_expenses()
            elif menu == '3':
                self.get_investment()
            elif menu == 'q' or menu == 'Q':
                break
            else:
                print('incorrect input please enter an item from the menu!')

        roi_total = Roi_calc()
        roi_total.runner()



