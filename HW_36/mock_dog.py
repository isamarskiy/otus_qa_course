import unittest
from HW_36.dog import get_sub_breeds, get_breeds
from unittest.mock import patch, Mock


class DogApi(unittest.TestCase):
    @patch('dog.requests.get')
    def test_all_breeds_list(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_breeds()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)

    def test_hound_sub_breeds(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('dog.requests.get')
        sub_breeds = [{
            "message": ["afghan", "basset", "blood", "english", "ibizan", "walker"],
            "status":"success"
        }]
        mock_get = mock_get_patcher.start()
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = sub_breeds
        response = get_sub_breeds()
        mock_get_patcher.stop()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), sub_breeds)


if __name__ == "__main__":
    unittest.main()
