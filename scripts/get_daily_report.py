from app.models import download_and_save_daily_report
import pendulum


def run(*args):
    if args:
        day = f"2022W{args[0]}5"  # todo: get input day
    else:
        day = None  # todo: current day
    download_and_save_daily_report(driver=True, sleep=5, headless=True, day=day)
