import unittest
from unittest.mock import patch, MagicMock
from basico import TestSeuBarriga

class UnitTestsForSeuBarriga(unittest.TestCase):

    def setUp(self):
        self.test_instance = TestSeuBarriga()

    def test_generate_new_user_format(self):
        email = self.test_instance.generate_new_user()
        self.assertRegex(email, r"^teste\d{8}_\d{6}@teste\.com$", "O email gerado não está no formato esperado")

    def test_generate_new_invoice_format(self):
        invoice = self.test_instance.generate_new_invoice()
        self.assertRegex(invoice, r"^Fatura do Aluguel - Vencimento \d{8}_\d{6}$", "A fatura gerada não está no formato esperado")

    @patch('selenium.webdriver.Chrome')
    @patch.object(TestSeuBarriga, 'generate_new_user')
    def test_register_and_login_flow(self, mock_generate_user, MockChrome):
        mock_driver = MagicMock()
        MockChrome.return_value = mock_driver
        
        # Mockando o comportamento do driver
        mock_driver.find_element.return_value = MagicMock()
        mock_generate_user.return_value = "teste20231022_123456@teste.com"
        
        self.test_instance.driver = mock_driver  # Atribua o mock driver à instância
        try:
            self.test_instance.test_register_and_login()
        except Exception as e:
            self.fail(f"test_register_and_login falhou devido a: {e}")

    @patch('selenium.webdriver.Chrome')
    @patch.object(TestSeuBarriga, 'generate_new_invoice')
    def test_add_invoice_flow(self, mock_generate_invoice, MockChrome):
        mock_driver = MagicMock()
        MockChrome.return_value = mock_driver
        
        # Mockando o comportamento do driver
        mock_driver.find_element.return_value = MagicMock()
        mock_generate_invoice.return_value = "Fatura do Aluguel - Vencimento 20231022_123456"
        
        self.test_instance.driver = mock_driver  # Atribua o mock driver à instância
        try:
            self.test_instance.add_invoice()
        except Exception as e:
            self.fail(f"add_invoice falhou devido a: {e}")

if __name__ == "__main__":
    unittest.main()
