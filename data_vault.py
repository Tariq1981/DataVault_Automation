

import sqlalchemy as sa
import sqlalchemy_teradata as sa_t
import pymysql as pym

engine=sa.create_engine("mysql+pymysql://root:@localhost:3306/ossn")
engine.connect()
meta=sa.MetaData()
meta.bind=engine
meta.reflect(engine)
meta.tables.keys()
user_test=sa.Table("TEST_USER",meta,
                   sa.Column("ID",sa.Integer()),
                   sa.Column("Name",sa.String(40))
                   )

user_test.create()




url=sa.engine.url.URL("teradata","dbc","dbc","192.168.226.130","1025","dbc")
print(url)
td_engine = sa.create_engine(url)
td_engine.connect()
res=td_engine.execute("SELECT * FROM DBC.Tables")
