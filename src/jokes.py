import requests


def _query_endpoint(
    endp:str, usr_agent:str, f:str,
    ) -> requests.models.Response:
    """Utility for formatting query string & requesting endpoint."""
    HEADERS = {
        "User-Agent": usr_agent,
        "Accept": f,
        }
    resp = requests.get(endp, headers=HEADERS, timeout=10)
    return resp

def _handle_response(r: requests.models.Response) -> str:
    """Utility for handling reponse object & returning text content."""
    if r.ok:
        c_type = r.headers["Content-Type"]
        if c_type == "application/json":
            content = r.json()
            content = content["joke"]
        elif c_type == "text/plain":
            content = r.text
        else:
            raise NotImplementedError(
                "This client accepts 'application/json' or 'text/plain' format"
                )
    else:
        raise requests.HTTPError(
            f"{r.status_code}: {r.reason}"
        )
    return content


def get_joke(
    endp:str = "https://icanhazdadjoke.com/",
    usr_agent:str = "Mozilla/...", 
    f:str = "text/plain",
) -> str:
    """Request a joke from icanhazdadjoke.com.

    Ask for a joke in either plain text or JSON format. Return the joke text.

    Parameters
    ----------
    endp : str, optional
        Endpoint to query, by default "https://icanhazdadjoke.com/"
    usr_agent : str, optional
        User agent value, by default ""Mozilla/...""
    f : str, optional
        Format to request eg "application.json", by default "text/plain"

    Returns
    -------
    str
        Joke text.
    """
    r = _query_endpoint(endp=endp, usr_agent=usr_agent, f=f)
    return _handle_response(r)
