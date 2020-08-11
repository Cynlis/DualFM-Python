import requests

class Now:
    def artist():
        url = "https://api.dualfm.net/stats"
        r = requests.get(url)
        res = r.json()['now']['artist']
        return res
    def song():
        url = "https://api.dualfm.net/stats"
        r = requests.get(url)
        res = r.json()['now']['song']
        return res
class Listeners:
    def current(id):
        url = "https://api.dualfm.net/stats"
        r = requests.get(url)
        res = r.json()['listeners']['current']
        return res
    def peak(id):
        url = "https://api.dualfm.net/stats"
        r = requests.get(url)
        res = r.json()['listeners']['peak']
        return res
class Presenter:
    def username(id):
        url = "https://api.dualfm.net/stats"
        r = requests.get(url)
        res = r.json()['presenter']['username']
        return res

