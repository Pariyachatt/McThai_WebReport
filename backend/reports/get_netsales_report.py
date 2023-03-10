from database.db_snowflake import *


class getNetsalesReport:
    def __init__(self):
        self.DB_USER_AUTH = 'MCTHAIDP.MC1.vw_Net_Sales_Report'
        self.DBSnowflake = DBSnowflake()


    def getReport(self):
        sql = """ select top 3 * from """+self.DB_USER_AUTH+"""; """
        # sql = """INSERT INTO """+self.DB_USER_AUTH+"""( USER_MAIL, PASSWORD, hint)VALUES('"""+self.mailAuth+"""', '"""+_passAuth+"""', '"""+hint+"""');"""

        return self.DBSnowflake.report_query(sql)
