import datetime
import logging
import unittest

from run import Data, MA, str2float, time_window


class TaxCalculationTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_str2float_handles_empty_and_commas(self):
        self.assertEqual(str2float(""), 0)
        self.assertEqual(str2float("1,234.56"), 1234.56)

    def test_time_window_keeps_rows_inside_range(self):
        rows = [
            Data("0700", "Tencent", "买入", "10", "100", "1000", "2025-01-02 10:00:00", "1", "港元"),
            Data("0700", "Tencent", "卖出", "5", "120", "600", "2026-01-02 10:00:00", "1", "港元"),
        ]

        result = time_window(rows, "20250101", "20251231")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].code, "0700")
        self.assertEqual(result[0].time, datetime.datetime(2025, 1, 2, 10, 0, 0))

    def test_moving_average_calculates_realized_gain_and_fees(self):
        rows = [
            Data("0700", "Tencent", "买入", "10", "100", "1000", datetime.datetime(2025, 1, 2), "1", "港元"),
            Data("0700", "Tencent", "卖出", "4", "130", "520", datetime.datetime(2025, 2, 2), "2", "港元"),
        ]

        tax_data = MA(rows, "20250101", "20251231")

        self.assertIsNotNone(tax_data)
        self.assertEqual(tax_data.code, "0700")
        self.assertEqual(tax_data.capital_gains, 120)
        self.assertEqual(tax_data.total_fee, 3)

    def test_moving_average_calculates_short_sell_gain(self):
        rows = [
            Data("TSLA", "Tesla", "卖空", "2", "250", "500", datetime.datetime(2025, 3, 1), "1", "美元"),
            Data("TSLA", "Tesla", "买入", "2", "220", "440", datetime.datetime(2025, 3, 2), "1", "美元"),
        ]

        tax_data = MA(rows, "20250101", "20251231")

        self.assertIsNotNone(tax_data)
        self.assertEqual(tax_data.capital_gains, 60)
        self.assertEqual(tax_data.total_fee, 2)


if __name__ == "__main__":
    unittest.main()
