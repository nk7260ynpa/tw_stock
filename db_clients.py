from sqlalchemy import create_engine, engine

def get_mysql_stock_conn() -> engine.base.Connection:
    """
    Get the connection to the MySQL database for stock data

    Parameters:
    ----------
    None

    Returns:
    ----------
    conn (engine.base.Connection): The connection to the MySQL database for stock data
    """
    address = "mysql+pymysql://root:root@172.27.0.2:3306/TaiwanStockExchange"
    engine = create_engine(address)
    conn = engine.connect()
    return conn

