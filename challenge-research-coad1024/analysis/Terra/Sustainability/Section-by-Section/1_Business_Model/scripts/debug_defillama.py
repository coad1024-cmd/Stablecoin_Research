
import requests

def check_defillama():
    url = "https://stablecoins.llama.fi/stablecoins"
    try:
        resp = requests.get(url)
        data = resp.json()
        pegged = data.get("peggedAssets", [])
        for p in pegged:
            if "terra" in p["name"].lower() or "ust" in p["symbol"].lower():
                print(f"Name: {p['name']}, Symbol: {p['symbol']}, ID: {p['id']}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check_defillama()
