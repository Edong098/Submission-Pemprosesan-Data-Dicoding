import unittest
from unittest.mock import patch, Mock
from utils.extract import fetching_content, scrape_main

class TestExtract(unittest.TestCase):

    @patch("utils.extract.requests.get")
    def test_fetching_content_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.text = "<html>TEST</html>"
        mock_get.return_value = mock_response

        result = fetching_content("https://example.com")
        self.assertEqual(result, "<html>TEST</html>")

    @patch("utils.extract.fetching_content")
    def test_scrape_main_return_list(self, mock_fetch):
        mock_fetch.return_value = """
        <div class="collection-card">
            <h3 class="product-title">Test Product</h3>
            <span class="price">$10</span>
            <p style="">Rating: 5</p>
            <p style="">3 Colors</p>
            <p style="">Size: M</p>
            <p style="">Gender: Men</p>
        </div>
        """

        BASE_URL = "https://example.com/?page={}"
        data = scrape_main(BASE_URL, start_page=1, end_page=1)

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Title"], "Test Product")

if __name__ == "__main__":
    unittest.main()