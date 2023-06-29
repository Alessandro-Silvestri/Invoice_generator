'''
INVOICE GENERATOR
Project by Alessandro Silvestri 2023
'''

'''
##### INPUT ##################################################

invoice_number
date
currency
invoice_from
invoice_to

INPUT list

row[
{
description: "describe the job done",
quantity: <1>,
rate: <price value>
amount: <amount value value showing the currency>
}
]

notes


##### OUTPUT ##################################################


invoice_number
date
invoice_from
address invoice_from
invoice_to
address invoice_to
rows

row[
{
description: "description",
quantity: <quantity>,
rate: <value>
amount: <amount value value showing the currency>
]
}

Total
'''

##### Program ##################################################
class Terminal_user_interface():
    def pretty_line(self, name:str, invoice_num,):
        space = " "
        invoice_num_len = len(str(invoice_num))
        space_num = 56 - len(name) - invoice_num_len
        return f"-"*67 + f"\n{name}{space*space_num}Invoice N. {invoice_num}"
    
    def user_inputs(self):
        # User Interface
        self.invoice_number = input("Invoice number: ")
        self.date = input("Date: ")
        self.invoice_from = input("Invoice from: ")
        self.invoice_from_address = input("Address: ")
        self.invoice_to = input("Invoice to: ")
        self.invoice_to_address = input("Address: ")
        self.rows = int(input("How many lines you need? "))

        # Loop for asking the main lines
        for i in range(self.rows):
            print(f"\n-----LINE {i+1} -----")
            self.desc = input("Insert description: ")
            self.quant = int(input("Insert quantity: "))
            self.rate = int(input("Insert rate: "))
            invoice.row(desc=self.desc, quant=self.quant, rate=self.rate)
        self.notes = input("\nInsert any notes: ")
    
    def output(self):
        print("\nInvoice number: ", self.invoice_number)
        print("Date: ", self.date)
        print("Invoice from: ", self.invoice_from)
        print("Address: ", self.invoice_from_address)
        print("Invoice to: ", self.invoice_to)
        print("Address: ", self.invoice_to_address)
        invoice.show_invoice()
        print(self.notes)


class InvoiceGenerator(Terminal_user_interface):
    def __init__(self):
        self.total = 0
        self.lines = []

    def row(self, desc:str, quant:int, rate:int):
        amount = quant * rate
        self.total += amount
        self.lines.append(f"{desc}, quantity: {quant}, rate: {rate}, amount: {amount}")
    
    def show_invoice(self):
        for i in self.lines:
            print(i)
        print(f"TOTAL: {self.total}")


invoice = InvoiceGenerator()
invoice.user_inputs()
invoice.output()


'''
Output I want:
-------------------------------------------------------------------
Invoice from:
<invoice from>                                    Invoice N.<value>
<address>

Invoice to:
<invoice_to>
<address>



item:                              quantity       rate       Amount
--------------------------------------------------------------------
Job description                           1        150 £       125 £  
--------------------------------------------------------------------
Job description                           1        150 £       125 £  
--------------------------------------------------------------------
Photo                                     1        150 £       125 £

                                                          TOTAL 375

Notes
<notes>

'''



'''
current OUTPUT:

Invoice number:  1
Date:  25/06/2023gi
Invoice from:  ALex
Invoice to:  Vanity
photo, quantity: 1, rate: 125, amount: 125
photo, quantity: 2, rate: 150, amount: 300
TOTAL: 425
banck account


'''


'''
invoice.row("photostudio", 2, 150)
invoice.row("photostudio", 1, 150)
invoice.row("photostudio", 2, 125)
invoice.row("photostudio", 1, 125)
invoice.show_invoice()
'''