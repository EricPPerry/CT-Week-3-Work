class ROICalc():
    #Define most variables that will be used, including all empty dictionaries, when class is first instanced 
    def __init__(self):
        self.expenses = 0
        self.expense_dict = {}
        self.total_expenses = 0
        self.p_count = 0
        self.p_name = ''
        self.income = 0
        self.income_dict = {} 
        self.total_income = 0
        self.cash_flow = 0
        self.cash_flow_dict = {}
        self.invest_dict = {}
        self.total_invest = 0
        self.target_roi = 0
        self.roi_dict = {}
        self.total_roi = 0
    
    def add_expense(self, cost):
        #instead of having separated functions for each expense, have one common expense function that adds on to the expense attribute 
        if cost == '':
            cost = 0
        self.expenses = self.expenses + int(cost)

    def get_expenses(self):
        #Function first gives the user the opportunity to define a target ROI, or leave it at the default - the average % gain from S&P 500 in the last decade
        print("Welcome to my calculator, where we determine your Cash on Cash Return on investment (CoC ROI)!")
        print("This is to be used on a potential property where you already know the hypothetical mortgage payments, to determine how much money you'd make once all expenses are accounted for.")
        while True:
            try:
                roi_target = input("First, what kind of ROI are you aiming for? Leave blank to compare it to the avg performance of the S&P 500: ")
                if roi_target == '' or roi_target == ' ':
                    roi_target = 13.6
                int(roi_target)
            except ValueError:
                print("Sorry, please enter a valid number or leave blank to use the S&P performance placeholder!")
                continue
            else:
                break
        self.target_roi = float(roi_target)




        #Goes through multiple input prompts to get expense amounts from user
        
        while True:
            self.p_count += 1
            choose_name = input(f"What is the name of this property? Leave blank to just use Property #{self.p_count}: ")
            if choose_name == '':
                self.p_name = self.p_count
            else:
                self.p_name = choose_name

            if input("Do you have an itemized list of expenses? Or jump straight to mortgage? Type (1) for itemized list and (2) to just input mortgage: ") == "1":
                #While loops used throughout as a quick way to make sure user is entering a valid number, and not letter/other character
                while True:
                    try:
                        response = input("How much are taxes per month on this property (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))
                

                while True:
                    try:
                        response = input("How much is monthly insurance on this property (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))


                while True:
                    try:
                        response = input("How much in utilties do you pay on this property (water/electric/gas combined)? (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))

                while True:
                    try:
                        response = input("Monthly HOA Fees on this property (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))


                while True:
                    try:
                        response = input("Monthly lawn/snow maintenance (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))

                while True:
                    try:
                        response = input("Monthly property management cost: (leave blank for $0)?: ")
                        if response == '' or response == ' ':
                            response = '0'
                        int(response)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break
                self.add_expense(int(response))

            while True:
                try:
                    response = input("What is the monthly mortgage payment for this property?: (leave blank for $0)?: ")
                    if response == '' or response == ' ':
                        response = '0'
                    int(response)
                except ValueError:
                    print("Sorry, please enter a valid number or leave blank for $0!")
                    continue
                else:
                    break
            self.add_expense(int(response))

            repeat_again = (input("Do you have another property?(Y/N): ")).lower()
            if repeat_again == 'y':
                my_ROI.next_property()        
            else:
                my_ROI.next_property()
                print("Here are the properties we're working with: ")
                for key, value in self.expense_dict.items():
                    print(f"Property: {key} // Expenses: ${value}")
                if self.p_count > 1:
                    print(f"# of Properties: {self.p_count} // Total Expenses: ${self.total_expenses}")
                break
    
    def add_income(self):
        
        #checks how many properties were entered, then iterates over each one, asking for # of units within each proeprty and breakdown of income each unit/property generates
        print("Alright, let's go over the income each of these properties generate...")
        for key in self.expense_dict:
            property_total_income = 0
            units = input(f"How many units are in property - {key}?: ")
            for u in range(int(units)):
                while True:
                    try:
                        property_rent = input(f"Rent collected for Unit {u+1} in property {key}: ")
                        if property_rent == '' or property_rent == ' ':
                            property_rent = 0
                        int(property_rent)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break


                while True:
                    try:
                        property_misc_income = input(f"Misc income (laundry/storage/etc.) for Unit {u+1} in property {key}: ")
                        if property_misc_income == '' or property_misc_income == ' ':
                            property_misc_income = 0
                        int(property_misc_income)
                    except ValueError:
                        print("Sorry, please enter a valid number or leave blank for $0!")
                        continue
                    else:
                        break

                #Total income generated by each unit/property is calculated and then added to the income dict, tracking income by property entered for further reference 
                property_total_income += (int(property_rent) + int(property_misc_income)) 

                self.total_income += int(property_rent)
                self.total_income += int(property_misc_income)
                self.income_dict[key] = property_total_income
        print("Income breakdown between properties", self.income_dict)
        print("Total income across all properties: $", self.total_income)


    def cashflow(self):
        #determine cashflow, total income minus total expenses
        #multiply it by 12 for annual_cashflow
        #for loop iterates through dictionary containing all previously entered properties, generates dictionary to have properties listed w/ their annual cashflow
        for key in self.expense_dict:
            self.cash_flow_dict[key] = ((self.income_dict[key] - self.expense_dict[key]) * 12)
        self.cash_flow = (self.total_income - self.total_expenses) * 12
        print(f"Here is what your cashflow looks like (what's left after you subtract your expenses from your income)")
        print(f"Monthly Cashflow: ${round(((self.cash_flow / 12)), 2)} // Annual Cashflow: ${round((self.cash_flow), 2)}") #updated rounding

    def cash_invest(self):
        #cash on cash income 
        #total_investment = how much money 'put in' - down payment, closing costs, rehab budget, misc other 
        print("Next, we need to know much cash you have already invested!")
        for key in self.expense_dict:
            property_investment = 0

            while True:
                try:
                    p_invest = input(f"What was the downpayment on the {key} property?(leave blank for 0): ")
                    
                    if p_invest == '' or p_invest == ' ':
                        p_invest = 0
                    int(p_invest)
                except ValueError:
                    print("Sorry, please enter a valid number or leave blank for $0!")
                    continue
                else:
                    break
            property_investment += int(p_invest)


            while True:
                try:
                    p_invest = input(f"What were the closing costs on the {key} property?(leave blank for 0): ")
                    if p_invest == '' or p_invest == ' ':
                        p_invest = 0
                    int(p_invest)
                except ValueError:
                    print("Sorry, please enter a valid number or leave blank for $0!")
                    continue
                else:
                    break
            property_investment += int(p_invest)



            while True:
                try:
                    p_invest = input(f"Any rehab/repair/misc costs to get property ready to rent (leave blank for 0): ")
                    if p_invest == '' or p_invest == ' ':
                        p_invest = 0
                    int(p_invest)
                except ValueError:
                    print("Sorry, please enter a valid number or leave blank for $0!")
                    continue
                else:
                    break
            property_investment += int(p_invest)
            #generates another dictionary so that the current cash investments can be referenced by future methods on a property by property basis
            self.invest_dict[key] = property_investment
        self.total_invest = sum(self.invest_dict.values())
        print("Breakdown of cash investments per property: ", self.invest_dict)
        print(f"Total investment across all properties: ${self.total_invest}")
    
    def roi_calc(self):
        #iterates through dictionary of property cashflower and calculates each property's ROI, generating another dict to track individual ROI
        for key, value in self.cash_flow_dict.items():
            self.roi_dict[key] = round(((value / self.invest_dict[key]) * 100), 2)
        print("Here are the ROI's for each property (% per year): ")
        #prints ROI dict for user review/reference
        for key, value in self.roi_dict.items():
            print(f"{key}  :  {value}%")
        #calculates the ROI of all properties combined, uses total cashflow and total investments instead of just averaging based on just the ROI
        self.total_roi = round(sum(self.cash_flow_dict.values()) / sum(self.invest_dict.values())*100, 2)
        print(f"The ROI between all your properties is: {self.total_roi}%")


        
    def final_roi(self):
        #determines best performing property based on ROI, then compares the average/total ROI of all properties vs. the user defined ROI target - or the default
        #has specific messages depending on the comparison, advising as to whether it is a good/bad investment (based on if it is better/worse than target ROI)
        print("Now it's the fun part, let's shed more light on how your ROI's are looking . . .")
        #quick check to see if there is only 1 property, so that responses/advice can be tailored correctly
        if len(self.roi_dict) > 1:
            best_property = max(self.roi_dict, key=self.roi_dict.get)
            best_roi = self.roi_dict[best_property]

            print(f"Your strongest performing property is: {best_property} with an ROI of: {best_roi}%")
            print(f"Again, your ROI between all properties is {self.total_roi}%")
            if self.total_roi > self.target_roi and self.target_roi != 13.6:
                print(f"When compared to your previously defined target ROI of {self.target_roi}%, yours outperforms it! This looks like a good investment.")
            elif self.total_roi < 0:
                print(f"Well....this isn't good. Your ROI is negative meaning owning these properties would LOSE you money....you really shouldn't pursue these properties.")
            elif self.total_roi < self.target_roi and self.target_roi != 13.6:
                print(f"When compared to your previously defined target ROI of {self.target_roi}%, yours performs worse. Maybe you should look at other properties!")
            elif self.target_roi == 13.6 and self.total_roi > self.target_roi:
                print(f"When compared to the avg S&P 500 performance in the last 10 years: {self.target_roi}% your properties do better! Looks like a good investment.")
            elif self.target_roi == 13.6 and self.total_roi < self.target_roi:
                print(f"When compared to the avg S&P 500 performance of the last 10 years: {self.target_roi}% your properties do worse. Maybe investing in stocks is a better play?")
        else:
            best_property = max(self.roi_dict, key=self.roi_dict.get)
            best_roi = self.roi_dict[best_property]
            print(f"Again, your ROI is {self.total_roi}%")
            if self.total_roi > self.target_roi and self.target_roi != 13.6:
                print(f"When compared to your previously defined target ROI of {self.target_roi}%, yours outperforms it! This looks like a good investment.")
            elif self.total_roi < 0:
                print(f"Well....this isn't good. Your ROI is negative meaning owning this property would LOSE you money......you really shouldn't pursue this property.")
            elif self.total_roi < self.target_roi and self.target_roi != 13.6:
                print(f"When compared to your previously defined target ROI of {self.target_roi}%, yours performs worse. Maybe you should look at other properties!")
            elif self.target_roi == 13.6 and self.total_roi > self.target_roi:
                print(f"When compared to the avg S&P 500 performance in the last 10 years: {self.target_roi}% your property does better! Looks like a good investment.")
            elif self.target_roi == 13.6 and self.total_roi < self.target_roi:
                print(f"When compared to the avg S&P 500 performance of the last 10 years: {self.target_roi}% your property does worse. Maybe investing in stocks is a better play?")

    


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
    my_ROI.final_roi()
   

       

run_calc()