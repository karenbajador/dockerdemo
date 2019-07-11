import unittest
import app

class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_main_page(self):
        response = self.app.post('/')
        assert response.status_code == 200
        assert b'Hello Wonderful World!' in response.data        

if __name__=='__main__':
    unittest.main()
