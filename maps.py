import requests
import time

def get_address_info(address):
    API_KEY = "GOOGLE MAPS API KEY HERE"
    API_URL = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(API_URL)
    data = response.json()
    return data

def main():
    address = input("Enter an address to locate it's coordinates: ")
    print("Loading information...")
    print("🕐")
    time.sleep(1)
    print("🕑")
    time.sleep(1)
    print("🕒")
    time.sleep(1)
    print("🕓")
    time.sleep(1)
    print("🕔")
    time.sleep(1)
    data = get_address_info(address)
    print("Relevant information:")
    if not data["results"]:
        print("No results found for the specified address.")
        suggestions = [result["formatted_address"] for result in data["suggestions"]]
        if suggestions:
            print("Did you mean one of these addresses?")
            for i, suggestion in enumerate(suggestions, 1):
                print(f"{i}. {suggestion}")
    else:
        result = data["results"][0]
        print(f"Formatted address: {result['formatted_address']}")
        view_location = input(f"Would you like to see the location of this address? (Y/N): ")
        if view_location.lower() == "y":
            print(f"Latitude: {result['geometry']['location']['lat']}")
            print(f"Longitude: {result['geometry']['location']['lng']} 🧭")
    print("\nDISCLAIMER: The information provided by this program is for reference purposes only and should not be used for any illegal activities.")

if __name__ == '__main__':
    main()
