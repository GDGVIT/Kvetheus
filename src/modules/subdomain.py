import sublist3r


def get_subdomains(domain):
    """Function to find all subdomains of a given domain."""
    try:
        resp = {"subdomains": []}
        subdomains = sublist3r.main(
            domain,
            ports=None,
            savefile=None,
            silent=False,
            verbose=False,
            threads=1000,
            enable_bruteforce=False,
            engines=None,
        )
        resp["subdomains"] = subdomains
        return resp

    except Exception as e:
        return {"error": str(e)}
