import yfinance as yf
from datetime import timedelta, datetime, date
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk


def create_ticker(ticker_key, current, last, comments, current_date, last_date):

    try:

        ticker = yf.Ticker(ticker_key).info
        current_price = ticker['regularMarketPrice']
        last_price = ticker['regularMarketPreviousClose']
        current.set(current_price)
        last.set(last_price)
        comments.delete("1.0", ctk.END)
        comments.insert("1.0", "CURR.|LAST")
        today = date. today()
        current_date.set(today.strftime("%d-%m-%Y"))
        last_date.set(today.strftime("%d-%m-%Y"))                            
    
    except KeyError:
        CTkMessagebox(title="Info", message="Ticker is not found.", icon="info")
    except Exception as e:
         CTkMessagebox(title="Info", message="Ticker is not found.", icon="info")  



def data_historical(ticker_key, start_date, entry_date):
    if not start_date or start_date.strip() == "":
        CTkMessagebox(title="Info", message="Select a valid date first.", icon="info")
        return
    

    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_parcial = start_date + timedelta(days=1)
    end_date = end_date_parcial.strftime("%Y-%m-%d")
    try:

        ticker = yf.Ticker(ticker_key)
        ticker_historical = ticker.history(start=start_date, end=end_date)
        close_price = ticker_historical['Close'][0]
        entry_date.set(close_price)
    except Exception as e:
            CTkMessagebox(title="Info", message="Ticker is not found.", icon="info")





