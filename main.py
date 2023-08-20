import sys
import logging

from datetime import timedelta, datetime

import aiohttp
import asyncio


class CurrencyRatePrinter:
    @staticmethod
    def print_currency_rate(date ,currency, data):
        rate = None
        for entry in data['exchangeRate']:
            if entry['currency'] == currency:
                rate = entry
                break
        # rate = next((entry for entry in data['exchangeRate'] if entry['currency'] == currency), None)

        if rate:
            logging.info(f"Exchange rate {currency} as of {date}: {rate['saleRate']} (sell) / {rate['purchaseRate']} (buy)")
        else:
            logging.info(f"{currency} is not found.")


def setup_log():
    logging.basicConfig(
        filename='file.log',
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    console_logger.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    root_logger = logging.getLogger()
    root_logger.addHandler(console_logger)

def input_data() -> int:
    input_line = sys.argv
    if int(input_line[1]) > 10:
        logging.error("You must enter a number less than 10.")
        sys.exit()
    return int(input_line[1])

def generate_date_list() -> list:
    today = datetime.now()
    date_list = [(today - timedelta(days=i)).strftime("%d.%m.%Y") for i in range(input_data())]
    return date_list

async def privatbank_request(session, date):
    async with session.get(f'https://api.privatbank.ua/p24api/exchange_rates?date={date}') as response:
        if response.status == 200:
            result = await response.json()
            return date, result
        else:
            logging.error("HTTP error: ", response.status)
            return None

async def main():
    setup_log()

    async with aiohttp.ClientSession() as session:
        tasks = [privatbank_request(session, date) for date in generate_date_list()]
        results = await asyncio.gather(*tasks)
        
        for date, data in results:
            if data:
                CurrencyRatePrinter.print_currency_rate(date,'USD', data)
                CurrencyRatePrinter.print_currency_rate(date, 'EUR', data)
                # logging.info(f"Exchange rates for {date}")
                # print(data)
            else:
                logging.error(f"The request for {date} failed ")

if __name__ == "__main__":
    asyncio.run(main())
    logging.shutdown()