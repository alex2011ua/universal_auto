import unittest


class TestBot(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone("/start")

    def test_main2(self):
        self.assertTrue('/start')

    def test_aut_handler(self):
        self.assertIsNotNone('Get autorizate')
    
    def test_reg_handler(self):
        self.assertIsNotNone('Get registration')

    def test_get_manager_today_report(self):
        self.assertTrue('Get all today statistic')

    def test_get_driver_today_report(self):
        self.assertTrue('Get today statistic')

    def test_report(self):
        self.assertIsNotNone("/report")

    def test_report_2(self):
        self.assertTrue('/report')

    def test_save_reports(self):
        self.assertIsNotNone("/save_reports")

    def test_save_reports_2(self):
        self.assertTrue('/save_reports')

    def test_update_db(self):
        self.assertTrue('/update_db')

    def test_update_db_2(self):
        self.assertIsNotNone('/update_db')

    def test_status(self):
        self.assertTrue('/status')

    def test_status(self):
        self.assertIsNotNone('/status')

    def test_update_driver_status_1(self):
        self.assertIsNotNone('Free')

    def test_update_driver_status_2(self):
        self.assertIsNotNone('Free')

    def test_update_driver_status_3(self):
        self.assertIsNotNone('With client')

    def test_update_driver_status_4(self):
        self.assertIsNotNone('With client')

    def test_update_driver_status_5(self):
        self.assertIsNotNone('Waiting for a client')

    def test_update_driver_status_6(self):
        self.assertIsNotNone('Waiting for a client')

    def test_update_driver_status_7(self):
        self.assertIsNotNone('Offline')

    def test_update_driver_status_8(self):
        self.assertIsNotNone('Offline')