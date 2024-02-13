from sqlalchemy import create_engine, engine

def get_mysql_stock_conn() -> engine.base.Connection:
    address = "mysql+pymysql://root:root@172.27.0.3:3306/Stock"
    engine = create_engine(address)
    conn = engine.connect()
    return conn

