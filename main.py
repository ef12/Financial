import stocksGetter as sg
import stocksAnalysis as sa

try:
    sg.get_store_tickers()
    sa.analyseStocks()
except ValueError:
    print("That's not a valid value for your age!")