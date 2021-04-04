class ROICalc():
#STILL NEED TO ADD DEFAULT VALUE OF ZERO FOR ALL INPUTS
#maybe just do a  while loop that breaks if the person did not put a valid number ?
# ADD SECTION WHERE USER INPUTS TARGET ROI, THEN AT END GIVES COMPARISON
    def __init__(self):
        self.expenses = 0
        self.expense_dict = {}
        self.total_expenses = 0
        self.p_count = 0
        self.p_name = ''
        self.income = 0
        self.income_dict = {} #WORK ON THIS MORE, it would allow individual ROI calculation, average ROI between properties, etc
        self.total_income = 0
        self.cash_flow = 0
        self.cash_flow_dict = {}
        self.invest_dict = {}
        self.total_invest = 0
        self.roi_dict = {}
        self.total_roi = 0
    
    def add_expense(self, cost):
        #maybe pass in the expense input/actions under this
        #change to 'get_expenses' ?
        if cost == '':
            cost = 0
        self.expenses = self.expenses + int(cost)

    def get_expenses(self): #MAYBE OFFER TO SKIP STRAIGHT TO MORTGAGE?!?!?!?!? -DONE
        print("Let's go over the expenses on this property, leave things blank if they are $0")
        while True:
            self.p_count += 1
            choose_name = input(f"What is the name of this property? Leave blank to just use Property #{self.p_count}: ")
            if choose_name == '':
                self.p_name = self.p_count
            else:
                self.p_name = choose_name

            if input("Do you have an itemized list of expenses? Or jump straight to mortgage? Type (1) for itemized list and (2) to just input mortgage: ") == "1":

                response = (input("How much were taxes on this property?: "))
                self.add_expense(response)
                response = (input("How much is insurance on this property?: "))
                self.add_expense(response)
                response = (input("How much are utilities (water/electric/gas combined): "))
                self.add_expense(response)
                response = (input("HOA Fees: "))
                self.add_expense(response)
                response = (input("Lawn/Snow Maintenance: "))
                self.add_expense(response)
                response = (input("Repairs needed when you bought the property: "))
                self.add_expense(response)
                response = (input("Property management cost: "))
                self.add_expense(response)
            response = (input("Monthly mortgage for this property: "))
            self.add_expense(response)
            repeat_again = (input("Do you have another property?(Y/N): ")).lower()
            if repeat_again == 'y':
                my_ROI.next_property()        
            else:
                my_ROI.next_property()
                print("Here are the properties we're working with: ")
                for key, value in self.expense_dict.items():
                    print(f"Property: {key} // Expenses: {value}")
                if self.p_count > 1:
                    print(f"# of Properties: {self.p_count} // Total Expenses: {self.total_expenses}")
                break
    
    def add_income(self):
        
        #checks how many properties were entered, then iterates over each one
        print("Alright, let's go over the income each of these properties generate...")
        for key in self.expense_dict:
            property_total_income = 0
            units = input(f"How many units are in property - {key}?: ")
            for u in range(int(units)):
                property_rent = int(input(f"Rent collected for Unit {u+1} in property {key}: "))
                property_misc_income = int(input(f"Misc income (laundry/storage/etc.) for Unit {u+1} in property {key}: "))
                property_total_income += (property_rent + property_misc_income) 

                self.total_income += property_rent
                self.total_income += property_misc_income
                self.income_dict[key] = property_total_income
        print("Income breakdown between properties", self.income_dict)
        print("Total income across all properties: $", self.total_income)
        #check how many units in the property
        #loop through same questions for each property - rent, misc: laundry, storage, etc (all as one??)

    def cashflow(self):
        #determine cashflow, total income minus total expenses
        #multiply it by 12 for annual_cashflow, to be used w/ conc
        for key in self.expense_dict:
            self.cash_flow_dict[key] = ((self.income_dict[key] - self.expense_dict[key]) * 12)
        self.cash_flow = (self.total_income - self.total_expenses) * 12
        print(f"Here is what your cashflow looks like (what's left after you subtract your expenses from your income)")
        print(f"Monthly Cashflow: {(self.cash_flow / 12)} // Annual Cashflow: {self.cash_flow}")

    def cash_invest(self):
        #cash on cash income 
        #total_investment = how much money 'put in' - down payment, closing costs, rehab budget, misc other 
        print("Next, we need to know much cash you have already invested!")
        for key in self.expense_dict:
            property_investment = 0
            property_investment += int(input(f"What was the downpayment on the {key} property?: "))
            property_investment += int(input(f"What were the closing costs on the {key} property?: "))
            property_investment += int(input(f"Any rehab/repair/misc costs to get property ready to rent: "))
            self.invest_dict[key] = property_investment
        self.total_invest = sum(self.invest_dict.values())
        print("Breakdown of cash investments per property: ", self.invest_dict)
        print(f"Total investment across all properties: ${self.total_invest}")
    
    def roi_calc(self):
        self.total_roi = round(((self.cash_flow / self.total_invest) * 100), 2)
        for key, value in self.cash_flow_dict.items():
            self.roi_dict[key] = round(((value / self.invest_dict[key]) * 100), 2)
        print("Here are the ROI's for each property: ", self.roi_dict)


        
    def final_roi(self):
        print("Now it's the fun part, revealing your ROI!!!")
        print("Again, your total cashflow across all properties is: $", self.cash_flow)
        print("Your total money already invested across all properties is: $", self.total_invest)

        #annual_cashflow / total investment * 100 = % annual ROI
    


    def next_property(self):
        self.total_expenses += self.expenses
        self.expense_dict[self.p_name] = self.expenses
        self.expenses = 0
        self.p_name = ''
        

        
my_ROI = ROICalc()


def run_calc():
    my_ROI.get_expenses()
    my_ROI.add_income()
    my_ROI.cashflow()
    my_ROI.cash_invest()
    my_ROI.roi_calc()
    #my_ROI.final_roi()
   

    
    #print("Total expenses is now: ", my_ROI.total_expenses)
   #print("Current property expenses: ", my_ROI.expenses)
    

run_calc()