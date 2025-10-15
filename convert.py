import requests

def convert_currency(from_currency, to_currency, amount, api_key):
    """
    Converts amount from one currency to another using CurrencyAPI.com.
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&base_currency={from_currency}&currencies={to_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("data") and to_currency in data["data"]:
            rate = data["data"][to_currency]["value"]
            result = amount * rate
            print(f"\n💱 {amount} {from_currency} = {result:.2f} {to_currency} (Rate: {rate:.4f})\n")
        else:
            print(f"❌ Conversion failed. Currency code '{to_currency}' may be invalid.\n")

    except requests.exceptions.Timeout:
        print("⏳ Request timed out. Check your internet connection.\n")
    except requests.exceptions.ConnectionError:
        print("🔌 Network error: Failed to connect to API.\n")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}\n")
    except ValueError:
        print("⚠️ Response could not be decoded as JSON.\n")
    except KeyError:
        print("⚠️ Unexpected response structure from API.\n")

if __name__ == "__main__":
    api_key = "cur_live_0VKBkJkakAk2M0hVt5h5o0T6MaKrAr8pNOYy3z0g"  # Your API key
    from_curr = input("From currency (e.g., USD): ").strip()
    to_curr = input("To currency (e.g., EUR): ").strip()
    amt_input = input("Amount to convert: ").strip()

    try:
        amt = float(amt_input)
        if amt <= 0:
            print("⚠️ Amount must be greater than zero.\n")
        else:
            convert_currency(from_curr, to_curr, amt, api_key)
    except ValueError:
        print("⚠️ Please enter a valid number for amount.\n")
