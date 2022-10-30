from app.models import Bolt


def run():
    b = Bolt(driver=True, sleep=3, headless=True)
    b.login()
    b.download_payments_order()
    b.save_report()