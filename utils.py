import datetime

def gen_date_list(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_list = [(start_date + datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, (end_date-start_date).days)]
    return date_list

if __name__ == "__main__":
    print(date_list("2021-01-01", "2021-01-05"))