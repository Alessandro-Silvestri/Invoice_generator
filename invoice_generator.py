'''
PYTHON INVOICE GENERATOR

Through the terminal interface the user can insert all the required data.
The integer input values are handled with exceptions.
Made by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>

##### bugs to fix ###########################################
add the currency
#############################################################

'''

class Terminal_user_interface():
    def pretty_header(self, name:str, invoice_num,):
        space = " "
        invoice_num_len = len(str(invoice_num))
        space_num = 56 - len(name) - invoice_num_len
        return f"-"*67 + f"\n{name}{space*space_num}Invoice N. {invoice_num}"
    
    def pretty_print_line(self, job, quantity, rate, amount):
        space = " "
        space1 = 43 - len(job) - len(str(quantity))
        space2 = 11 - len(str(rate))
        space3 = 14 - len(str(amount))
        return f"{job}{space*space1}{quantity}{space*space2}{rate}{space*space3}{amount}"
    
    def pretty_total(self, t):
        space = " "
        spaces = 61 - len(str(t))
        return f"{space*spaces}TOTAL: {t}"
    
    def error(self):
        print("Error: wrong value\n")

    def user_inputs(self):
        # ask the invoice number
        while True:
            try:
                self.invoice_number = int(input("\nInvoice number: "))
                break
            except ValueError:
                self.error()
        self.date = input("Date: ")
        self.invoice_from = input("\nInvoice from: ")
        self.invoice_from_address = input("Address: ")
        self.invoice_to = input("\nInvoice to: ")
        self.invoice_to_address = input("Address: ")
        # ask the number of lines
        while True:
            try:
                self.rows = int(input("How many lines you need? "))
                break
            except ValueError:
                self.error()
        # Loop for asking the main lines
        for i in range(self.rows):
            print(f"\n-----LINE {i+1}/{self.rows} -----")
            self.desc = input("Insert description: ")
            # ask the quantity
            while True:
                try:
                    self.quant = int(input("Insert quantity: "))
                    break
                except ValueError:
                    self.error()
            # ask the rate
            while True:
                try:
                    self.rate = int(input("Insert rate: "))
                    break
                except ValueError:
                    self.error()
            invoice.row(desc=self.desc, quant=self.quant, rate=self.rate)
        self.notes = input("\nInsert any notes: ")
        print("\n\n\n")

    def output(self):
        # header
        print(self.pretty_header(self.invoice_from, self.invoice_number))
        print(self.invoice_from_address)
        print(f"\n\nINVOICE TO:\n{self.invoice_to}\n{self.invoice_to_address}")
        # main lines
        print("\n\n\n\n\nITEM:                              QUANTITY       RATE        AMOUNT")
        print("-"*68)
        for i in range(len(self.lines)):
            print(self.pretty_print_line(self.lines[i][0], self.lines[i][1], self.lines[i][2], self.lines[i][3]))
            print("-"*68)
        # total
        print(self.pretty_total(self.total))
        print("\n\n\n")
        print(f"Notes:\n{self.notes}")
        print("-"*68)
        print("\n\n\n\n")


class InvoiceGenerator(Terminal_user_interface):
    def __init__(self):
        self.total = 0
        self.lines = []

    def row(self, desc:str, quant:int, rate:int):
        amount = quant * rate
        self.total += amount
        self.lines.append([desc, quant, rate, amount])


invoice = InvoiceGenerator()
invoice.user_inputs()
invoice.output()
