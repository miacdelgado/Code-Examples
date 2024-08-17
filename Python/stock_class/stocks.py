class Stock():
    def __init__(self,symbol,company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
    
def add_stock_to_purchase_history(stock, stockTable):
    stockTable[stock.get_symbol()] = stock.get_company_name()

def stock_purchace_history():
    stockTable = {}
    symbols = ['AAPL', 'CAT', 'EK', 'GOOG', 'MSFT']
    company_names = ['Apple Inc', 'Caterpillar', 'Eastman Kodak', 'Google', 'Microsoft']

    for i, key in enumerate(symbols):
        stockTable[key] = company_names[i]

    print("Stock Purchase History: ")
    print("Symbol | Company Name ")
    for key, val in stockTable.items():
        print(key, ' | ', val)
    