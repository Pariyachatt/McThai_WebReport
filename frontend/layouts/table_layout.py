import streamlit as st
from st_aggrid import AgGrid
from database.db_snowflake import *

from frontend.functions.cal import *
from backend.reports.get_netsales_report import *

# from snowflake.sqlalchemy import URL


with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


class TableLayouts:
    def __init__(self):
        self.getNetsalesR = getNetsalesReport()

    def reportGrid(self, s_date, e_date):
        yearCurr = str(s_date.year)
        yearOld = str(s_date.year-1)
        columnDefs = [
            {"headerName": "",
                "children": [
                    { "headerName": "Date", "field": "Date", "sortable": True},
                    {"headerName": "Day", "field": "Day","sortable": True},
                    {"headerName": "Profit Name","field": "profit_name", "sortable": True},
                    {"headerName": "Patch Name", "field": "patch_name", "sortable": True},
                    {"headerName": "Store Code", "field": "store_code", "sortable": True},
                    {"headerName": "Store Name", "field": "store_name", "sortable": True}
                ]
             },
            {"headerName": "31Q Plan",
                "children": [
                    {"headerName": "Sales Target","field": "Sales Target", "sortable": True},
                    {"headerName": "Accum Sales","field": "Accum Sales", "sortable": True}
                ]
             },
            {"headerName": "Actual "+yearCurr,
                "children": [
                    {"headerName": "Sales", "field": "CY Sales","sortable": True},
                    {"headerName": "Accu Sales","field": "CY Accu Sales", "sortable": True},
                    {"headerName": "GC","field": "CY GC", "sortable": True},
                    {"headerName": "Accu GC", "field": "CY Accu GC","sortable": True},
                    {"headerName": "AC", "field": "CY AC", "sortable": True}
                ]
             },
            {"headerName": "Actual "+yearOld,
                "children": [
                    {"headerName": "Sales", "field": "LY Sales", "sortable": True},
                    {"headerName": "Accu Sales","field": "ly_accu_sales", "sortable": True},
                    {"headerName": "GC","field": "LY GC", "sortable": True},
                    {"headerName": "Accu GC", "field": "LY Accu GC", "sortable": True},
                    {"headerName": "AC", "field": "LY AC", "sortable": True}
                ]
             },
            {"headerName": "% Comp. MTD",
                "children": [
                    {"headerName": "Sales","field": "p_comp_sales", "sortable": True},
                    {"headerName": "GC","field": "p_comp_gv", "sortable": True}
                ]
             },
            {"headerName": "% Achiev",
                "children": [
                    {"headerName": "Sales", "field": "%Achieve Sales", "sortable": True}
                ]
             }
        ]
        options = {"columnDefs": columnDefs,
                   "groupIncludeTotalFooter": True,
                   "groupIncludeFooter": True,
                   "paginationPageSize": 50,
                   "pagination": True,
                   "defaultExcelExportParams": JsCode("""
                        funtion (params) {
                            const isRootLevel = params.node.level == -1;
                            console.log('test',params.node);
                            if (isRootLevel) {
                                return 'Total Sales';
                            }
                        }""")
                    }

        # sqlRespReport = self.getNetsalesR.getReport(str(s_date), str(e_date), True)
        sqlRespReport = self.getNetsalesR.getReport(str(s_date), str(e_date))
        # st.write(sqlRespReport)
        # df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
        AgGrid(sqlRespReport, gridOptions=options, allow_unsafe_jscode=True)
