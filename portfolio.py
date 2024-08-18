from datetime import datetime
import random

class Stock:
    def __init__(self) -> None:
        self.historic = {}
        for month_numbre in range(1, 12+1):
            for day_number in range(1,30 + 1):
                current_date = f'2024-{month_numbre:02d}-{day_number:02d}'
                self.historic[current_date] = random.randint(17, 20)
    
    def get_price(self, date:str) -> int:
        return self.historic[date]

class Portfolio:
    def __init__(self, purchase_portfolio_date:str, stocks_diversification:dict, investment: int) -> None:
        sum_percentage = sum(stocks_diversification.values())
        if int(sum_percentage) != 1:
            print(sum_percentage)
            print("The percentages to invest do not add up to 1.")
            return None
        self.purchase_portfolio_date = purchase_portfolio_date
        self.historic = {}
        self.investment = investment

        self.stocks_available = {}

        for stock_name in stocks_diversification.keys():
            self.stocks_available[stock_name] = Stock()

        self.my_stocks = {}
        for stock_name, per_stock in stocks_diversification.items():
            self.my_stocks[stock_name] = self.get_stocks_depending_current_price(per_stock, investment, self.stocks_available[stock_name])

    def get_stocks_depending_current_price(self, per_stock:float, total_investment: int, stock_obj:Stock) -> float:
        mount_to_invest_in_stock = total_investment*per_stock
        current_price_stock = stock_obj.get_price(self.purchase_portfolio_date)
        n_stocks = mount_to_invest_in_stock/current_price_stock
        return n_stocks

    def get_portfolio_value_by_date(self, date:str) -> float:
        value_portfolio = 0
        for key_stock, n_stocks in self.my_stocks.items():
            price_stock_by_date = self.stocks_available[key_stock].get_price(date)
            value_portfolio += price_stock_by_date*n_stocks
        return value_portfolio

    def profit(self, init_date:str, final_date:str) -> None:
        if init_date < self.purchase_portfolio_date:
            print(f"The start date is before the acquisition of your portfolio. Taking start date as {self.purchase_portfolio_date}")
            init_date = self.purchase_portfolio_date
        try:
            init_value_portfolio = self.investment
            final_value_portfolio = self.get_portfolio_value_by_date(final_date)
            profit = final_value_portfolio - init_value_portfolio
            profit_percentage =round((profit)/init_value_portfolio, 2)
            annualized_return = self.profit_annualized(init_date, final_date, profit_percentage)
            print(f"Init value portfolio [{init_date}]: {init_value_portfolio}")
            print(f"Current value portfolio [{final_date}]: {final_value_portfolio}")
            print(f"Profit [{final_date}]: {profit}")
            print(f"Current rentability [{final_date}]: {profit_percentage} = {round(profit_percentage*100, 2)}%")
            print(f"Annualized return: {round(annualized_return, 2)} = {round(annualized_return*100, 2)}%")
        except Exception as e:
            print(f"Error with the dates: \n{e}")

    def profit_annualized(self,init_date:str, final_date:str, rentability_betwen_dates:float) -> float:
        date_format = "%Y-%m-%d"
        init_date_obj = datetime.strptime(init_date, date_format).date()
        final_date_obj = datetime.strptime(final_date, date_format).date()
        difference_days = (final_date_obj - init_date_obj).days
        print(difference_days)
        n = difference_days/365
        annualized_return = ((1 + rentability_betwen_dates)**(1/n)) - 1
        return annualized_return


if __name__ == "__main__":
    init_date = "2024-01-01"
    final_date = "2024-12-30"
    total_investement = 100
    stocks_diversification = {"stock_a": 0.3, "stock_b": 0.4, "stock_c": 0.3}
    port_obj = Portfolio(init_date, stocks_diversification, total_investement)
    print(f"\nINFORMATION:")
    port_obj.profit(init_date, final_date)

