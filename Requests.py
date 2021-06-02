import requests
class Request(object):
    def __init__(self, base):
        self.base = base

    def send_post(self, end_point, data):
        try:
            r = requests.post(url=self.base+end_point, data=data)
            if r.status_code == 200:
                data = r.json()
                return data
            else:
                print('Error sending post')
        except requests.exceptions.HTTPError as err:
            print(err.response.text)
        except requests.exceptions.ConnectionError as err:
            print("Error connecting:", err)


    def send_get(self, end_point, header):
        try:
            r = requests.get(self.base+end_point,headers=header)
            if r.status_code == 200:
                data = r.json()
                return data
        except requests.exceptions.HTTPError as err:
            print(err.response.text)
        except requests.exceptions.ConnectionError as err:
            print("Error connecting:", err)








