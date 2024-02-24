import pandas as pd
import utils
import twse_crawler 

def test_gen_date_list():
    assert utils.gen_date_list("2021-01-01", "2021-01-05") == ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04']

