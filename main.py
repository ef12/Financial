import stocksGetter as sg
import stocksAnalysis as sa
import emailPropose as ep
try:
    sg.get_store_tickers()
    sa.analyseStocks()
    ep.get_propose_and_email()
except ValueError:
    print("Error")