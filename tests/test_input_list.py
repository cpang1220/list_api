from tests.setting import Setting
import json
from unittest.mock import patch
import app.list_sum as list_sum


class TestUser(Setting):
    def test_get_input_list(self):
        """
        Test to retrieve input list
        :return:
        """
        with self.client:
            response = self.client.get(
                '/input_list'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == 'success')
            self.assertIsInstance(data['input_list'], list)
            self.assertEqual(len(data['input_list']), 10000001)

    def test_get_input_list_sum(self):
        """
        Test to retrieve the sum of input list
        :return:
        """
        with self.client:
            response = self.client.get(
                '/total'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == 'success')
            self.assertIsInstance(data['total'], int)
            self.assertEqual(data['total'], 50000005000000)

    @patch.object(list_sum, 'get_list_sum')
    @patch('app.const.HTTP_ERROR', True)
    def test_get_input_list_sum_error(self, mock_get_list_sum):
        """
        Test to retrieve the sum of input list with 404 error
        :return:
        """
        mock_api_result = {
            'message': 'input list not found',
            'status_code': 404
        }
        mock_get_list_sum.return_value = mock_api_result
        with self.client:
            response = self.client.get(
                    '/total'
                )
            self.assertTrue(mock_get_list_sum.called)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data['status'] == 'HTTP error')
            self.assertTrue(data['message'] == 'input list not found')
