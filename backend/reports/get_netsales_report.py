from database.db_snowflake import *


class getNetsalesReport:
    def __init__(self):
        self.DB_USER_AUTH = 'Net_Sales_Report_UDF'
        self.DBSnowflake = DBSnowflake()

    def getReport(self, s_date, e_date, profit="", patch="", store="", debug=False):
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
        FROM TABLE("""+self.DB_USER_AUTH+"""('"""+s_date+"""'::DATE,'"""+e_date+"""'::DATE,'[''"""+profit+"""'']' """+patch+""" """+store+""")) AS Net_Sales_Report
      ORDER BY 1,2,3,4
      ;"""
        if debug:
            st.write("getReport: ", sql)
        return self.DBSnowflake.report_query(sql)
