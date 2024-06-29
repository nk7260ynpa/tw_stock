from sqlalchemy import create_engine, engine

def get_mysql_stock_conn() -> engine.base.Connection:
    address = "mysql+pymysql://root:root@127.0.0.1:3306/TaiwanStockExchange"
    engine = create_engine(address)
    conn = engine.connect()
    return conn

