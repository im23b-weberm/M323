import unittest
from main import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode('utf-8'), 'Willkommen bei meiner Flask-App!'
        )

    def test_info(self):
        response = self.client.get('/info')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Dies ist die Info-Seite.')

    def test_user(self):
        response = self.client.get('/user/John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hallo, John!')

    def test_post_data(self):
        response = self.client.post('/post')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Daten erfolgreich erhalten!')

    def test_feedback_get(self):
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.decode('utf-8'), 'Bitte geben Sie Ihr Feedback ab.'
        )

    def test_feedback_post(self):
        response = self.client.post('/feedback')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Danke für Ihr Feedback!')

    def test_item(self):
        response = self.client.get('/item/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Artikel-ID: 123')
