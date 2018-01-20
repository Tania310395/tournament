import unittest
import requests
import json
import random
import string


BASE_URL = 'http://localhost:8888'
random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])


class BaseSwissTest(unittest.TestCase):

    def setUp(self):
        auth = {
            'username': random,
            'password': 'hello123',
            'first_name': 'Tania',
            'country_name': 'India'
        }
        r = requests.post(
            "{}/api/signup/".format(BASE_URL),
            json=auth
        )
        data = self.resp_to_json(r)
        self.token = data['token']

    def resp_to_json(self, r):
        return json.loads(r.content.decode('utf-8'))

    def tearDown(self):
        requests.delete(
            "{}/api/reset_db/".format(BASE_URL)
        )


class LoginTest(BaseSwissTest):
    def test_hello_view(self):
        payload = {'username': 'u1', 'password': 'hello123'}
        r = requests.get("{}/api/hello/".format(BASE_URL), headers={
            'X-Auth-Token': self.token
        }, json=payload)
        data = self.resp_to_json(r)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(data['hello'], 'world')
        r = requests.get("{}/api/hello/".format(BASE_URL), headers={
        }, json=payload)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(self.resp_to_json(r)['error'], "token not supplied")


class CreateTournamentTest(BaseSwissTest):

    def test_create_tournament(self):
        payload = {'name': 'ipl'}
        r = requests.post("{}/api/home".format(BASE_URL), headers={
            'X-Auth-Token': self.token
        }, json=payload)
        self.assertEqual(r.status_code, 200)
        content = self.resp_to_json(r)
        self.assertEqual(content['name'], payload['name'])


if __name__ == '__main__':
    unittest.main()
