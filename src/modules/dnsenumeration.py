import dns.resolver
import re, requests


def add_to_dict(dict_obj, key, value):
    """
    Utility function to add the results to the dictionary and handles duplicacy.
    """
    if key not in dict_obj:
        dict_obj[key] = value
    elif isinstance(dict_obj[key], list):
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [dict_obj[key], value]

    return dict_obj


def fetch_CNAMErecords(target):
    """Function to get all CNAME records for a domain (especially for Cloudflare)"""

    headers = {
        "Pragma": "no-cache",
        "Origin": "https://dnsdumpster.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,it;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cache-Control": "no-cache",
        "Referer": "https://dnsdumpster.com/",
        "Connection": "keep-alive",
        "DNT": "1",
    }

    get_csrf_res = requests.get("https://dnsdumpster.com", headers=headers)

    try:
        csrf_token = get_csrf_res.headers["Set-Cookie"]
        csrf_token = csrf_token[10:]
        csrf_token = csrf_token.split(";")[0]
    except Exception as e:
        print("Retrieving CSRF Token for DNSDumpster failed")
        return

    cookies = {
        "csrftoken": csrf_token,
    }

    data = [("csrfmiddlewaretoken", csrf_token), ("targetip", target), ("user", "free")]

    res = requests.post(
        "https://dnsdumpster.com/", headers=headers, cookies=cookies, data=data
    )
    try:
        scraped = res.text
        subdomain_finder = re.compile('">(.*\.' + target + ")<br>")
        links = subdomain_finder.findall(scraped)

    finally:
        return links


def get_records(domain):
    """
    Get all the records associated with a domain.
    """
    result = {}

    # List of all types of existing records for a domain.
    types = [
        "A",
        "NS",
        "MD",
        "MF",
        "CNAME",
        "SOA",
        "MB",
        "MG",
        "MR",
        "NULL",
        "WKS",
        "PTR",
        "HINFO",
        "MINFO",
        "MX",
        "TXT",
        "RP",
        "AFSDB",
        "X25",
        "ISDN",
        "RT",
        "NSAP",
        "NSAP-PTR",
        "SIG",
        "KEY",
        "PX",
        "GPOS",
        "AAAA",
        "LOC",
        "NXT",
        "SRV",
        "NAPTR",
        "KX",
        "CERT",
        "A6",
        "DNAME",
        "OPT",
        "APL",
        "DS",
        "SSHFP",
        "IPSECKEY",
        "RRSIG",
        "NSEC",
        "DNSKEY",
        "DHCID",
        "NSEC3",
        "NSEC3PARAM",
        "TLSA",
        "HIP",
        "CDS",
        "CDNSKEY",
        "CSYNC",
        "SPF",
        "UNSPEC",
        "EUI48",
        "EUI64",
        "TKEY",
        "TSIG",
        "IXFR",
        "AXFR",
        "MAILB",
        "MAILA",
        "ANY",
        "URI",
        "CAA",
        "TA",
        "DLV",
    ]

    for Type in types:
        try:
            answers = dns.resolver.resolve(domain, Type)
            for rdata in answers:
                # Adds data to the result.
                result = add_to_dict(result, Type, rdata.to_text())

        except Exception as e:
            pass  # or pass

    try:
        # Try to fetch CNAME records (if any)
        cname = fetch_CNAMErecords(domain)
        for records in cname:
            result = add_to_dict(result, "CNAME", records)

    except Exception as e:
        pass  # or pass

    finally:
        return result
