import requests

def convert_currency(from_currency, to_currency, amount):
    """
    Converts a specified amount from one currency to another using exchangerate.host API.

    Args:
        from_currency (str): The currency code to convert from (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'EUR').
        amount (float): The amount of currency to convert.

    Returns:
        None. Prints the conversion result or error messages to the console.
    """
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            rate = data["info"]["rate"]
            result = data["result"]
            print(f"\n💱 {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()} (Rate: {rate:.4f})")
        else:
            print("❌ Conversion failed. Please check the currency codes and try again.")

    except requests.exceptions.RequestException as e:
        print("🔌 Network error:", e)
    except KeyError:
        print("⚠️ Unexpected response structure. Please try again later.")


if __name__ == "__main__":
    """
    Main entry point for the currency converter app.
    Prompts the user for input and performs currency conversion.
    """
    from_curr = input("From currency (e.g., USD): ").strip().upper()
    to_curr = input("To currency (e.g., EUR): ").strip().upper()
    try:
        amt = float(input("Amount to convert: "))
        convert_currency(from_curr, to_curr, amt)
    except ValueError:
        print("⚠️ Please enter a valid number for amount.")
