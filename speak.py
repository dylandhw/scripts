import requests 

def check_internet(url="https://www.google.com", timeout=5):
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False 
    except requests.Timeout:
        return False 
