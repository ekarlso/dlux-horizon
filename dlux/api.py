import requests


from odlclient.v2 import client as odl_client


def get_client(request):
    session = requests.Session()
    session.cookies.update({
        'JSESSIONID': request.user.jsessionid,
        'JSESSIONIDSSO': request.user.jsessionidsso
    })
    url = request.user.controller + '/controller/nb/v2'
    http = odl_client.HTTPClient(url, http=session)
    client = odl_client.Client(http)
    return client
