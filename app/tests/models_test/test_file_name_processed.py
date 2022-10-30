import pytest
from app.models import FileNameProcessed

fnp = FileNameProcessed()


@pytest.mark.django_db
def test_file_name_processed_create():
    file_name_processed = FileNameProcessed.objects.create(
        filename_weekly="20230829-20220904-payments_driver-___.csv")
    assert file_name_processed.filename_weekly == "20230829-20220904-payments_driver-___.csv"
    assert FileNameProcessed.objects.count() == 1


@pytest.mark.django_db
def test_save_data_to_db():
    test_file_name_processed = ['20220829-20220904-payments_driver-___.csv',
                                'Bolt Weekly Report - 2022W37 - Kyiv Fleet 03_232 park Universal-auto.csv']

    fnp.save_filename_to_db(processed_files=test_file_name_processed)
    assert True

