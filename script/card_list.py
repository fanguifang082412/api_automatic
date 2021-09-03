import unittest
import requests
from hy_api.api_all import HyApi


class RechargeUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()
        cls.hy_api = HyApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.hy_api.get_login_url(self.session, "心悦有限公司", "123456", "8888")

    def tearDown(self) -> None:
        self.session.close()

    def test_card_list(self):
        response = self.hy_api.get_card_list(self.session)
        self.assertEqual(200, response.status_code)



if __name__ == "__main__":
    unittest.main()
