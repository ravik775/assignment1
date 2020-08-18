from SentenceExpanse import WordTransulator
import unittest


class TestTransulateMethods(unittest.TestCase):

    def setUp(self):
        self.instance = WordTransulator()

    def test_transulate_word(self):
        test_data = {
            "telephone": ["mobile", "landline"],
            "ph": ["telephone"]
        }
        for test_input, expected_result in test_data.items():
            expected_result.sort()
            test_result = sorted(self.instance.transulate_word(test_input))
            self.assertEqual(expected_result, test_result, "Transulations are not as expected.")
        
    def test_transulate_word_no_mapping(self):
        self.assertIsNone(self.instance.transulate_word("test_input"))
        
    def test_simple_transulation(self):
        test_data = {
            "NH #: 44": ["National HighWay Number: 44"],
            "ph #: +91-9848012345": ["telephone Number: +91-9848012345", "mobile Number: +91-9848012345", "landline Number: +91-9848012345"]
        }
        for test_input, expected_result in test_data.items():
            expected_result.sort()
            test_result = sorted(self.instance.transulate(test_input))
            self.assertEqual(expected_result, test_result, "Transulations are not as expected.")
        
if __name__ == '__main__':
    unittest.main()