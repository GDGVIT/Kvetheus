import requests


def get_whois(domain):
    """Fetch WHOIS information for a domain"""

    headers = {"referer": "https://whoisjson.com/whois-api"}

    try:
        resp = requests.get(
            "https://whoisjson.com/API/website?domain=" + domain, headers=headers
        )
        return resp.text

    except Exception as e:
        print(e)
