from database.db_snowflake import *


class getNetsalesReport:
    def __init__(self):
        self.DB_USER_AUTH = 'MCTHAIDP.MC1.vw_Net_Sales_Report'
        self.DBSnowflake = DBSnowflake()

    def getReport(self, s_date, e_date, profit="", debug=False):
        # sql = """ SELECT top 3 "Date", "Day",
        profit_con = ""
        if profit:
            profit_con = " AND PROFIT_NAME='"+profit+"'"

        sql = """ SELECT "Date", "Day",
        PROFIT_NAME,
        PATCH_NAME,
        STORE_CODE,
        "STORE NAME" as STORE_NAME,
        "Sales Target",
        "Accum Sales",
        "CY Sales",
        "CY Accu Sales",
        "CY GC",
        "CY Accu GC",
        "CY AC",
        "LY Sales",
        "LY Accu Sales" AS ly_accu_sales,
        "LY GC",
        "LY Accu GC",
        "LY AC",
        "% Comp. Sales" AS p_comp_sales,
        "% Comp. GC" AS p_comp_gv,
        "%Achieve Sales"
        FROM """+self.DB_USER_AUTH+"""
        WHERE "Date" BETWEEN '"""+s_date+"""'
        AND '"""+e_date+"""'
        """+profit_con+"""
        ;"""
        if debug:
            st.write("getReport: ", sql)
        return self.DBSnowflake.report_query(sql)
