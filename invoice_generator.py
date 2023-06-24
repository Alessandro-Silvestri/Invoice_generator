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
invoice_to

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
class InvoiceGenerator():
    def __init__(self) -> None:
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
invoice.row("photostudio", 2, 150)
invoice.row("photostudio", 1, 150)
invoice.row("photostudio", 2, 125)
invoice.row("photostudio", 1, 125)
invoice.show_invoice()