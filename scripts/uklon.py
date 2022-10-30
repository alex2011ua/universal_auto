from app.models import Uklon


def run():
    b = Uklon(driver=True, sleep=3, headless=True)
    b.login()
    b.download_payments_order()
    b.save_report()