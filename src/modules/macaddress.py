import requests


def MacAddressLookup(mac):
    """
    This function will look up the mac address in the mac address database.
    """
    try:
        response = requests.get("https://macvendors.co/api/" + mac)
        result = response.json()
        if result["result"]:
            return result
        else:
            return {"error": "Something Went Wrong!"}

    except Exception as e:
        return {"error": str(e)}
