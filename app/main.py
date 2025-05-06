from scraper import fetch_prices
from pricing import calculate_fair_price
from ai_description import generate_description

def main():
    item = input("Enter the item name: ")

    print("\n Fetching prices...")
    prices = fetch_prices(item)
    print(f"Found prices: {prices}")

    fair_price = calculate_fair_price(prices)
    print(f" Suggested price: £{fair_price}")

    print("\n Generating description...")
    description = generate_description(item)
    print(f"\n Description:\n{description}")

if __name__ == "__main__":
    main()
