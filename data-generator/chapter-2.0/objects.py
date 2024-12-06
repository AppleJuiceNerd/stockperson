import datetime

# Represents a product
class Product:
    def __init__(self, name: str, price: float):

        self.name = name
        self.price = price

# Represents a line in an invoice
class InvoiceLine:
    def __init__(
        self,
        lineNo: int,
        product: Product,
        quantity: int,
    ):

        self.lineNo = lineNo
        self.product = product
        self.quantity = quantity


# Represents a sales invoice
class Invoice:
    def __init__(
        self,
        docNo: str,
        date: datetime.date,
        customer: str,
        discount: float,
        lines: list,
    ):

        self.docNo = docNo
        self.date = date
        self.customer = customer
        self.lines = lines
