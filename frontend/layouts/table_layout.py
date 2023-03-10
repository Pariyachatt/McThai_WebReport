import streamlit as st
from st_aggrid import AgGrid

from database.db_snowflake import *
from frontend.functions.cal import *

from backend.reports.get_netsales_report import *

from snowflake.sqlalchemy import URL


with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


class TableLayouts:
    def __init__(self):
        self.getNetsalesR = getNetsalesReport()
        self.resReport = self.getNetsalesR.getReport()

        # st.write(self.resReport)


    def reportGrid(self, s_date, e_date):
        # for i in self.resReport:
        #     st.write("reportGrid:", i)
        #
        # df = pd.DataFrame(self.resReport)
        # st.table(df)
        # df = pd.DataFrame(
        #    np.random.randn(10, 5),
        #    columns=('col %d' % i for i in range(5)))
        #
        # st.table(df)

        # st.write(self.resReport)
        yearCurr = str(s_date.year)
        yearOld = str(s_date.year-1)

        columnDefs = [
            {"headerName": "",
                "children": [
                    { "headerName": "Date", "field": "Date", "sortable": True},
                    {"headerName": "Day", "field": "Day","sortable": True},
                    {"headerName": "Profit name","field": "PROFIT_NAME", "sortable": True},
                    {"headerName": "Patch name", "field": "PATCH_NAME", "sortable": True},
                    {"headerName": "Store code", "field": "STORE_CODE", "sortable": True},
                    {"headerName": "Store name", "field": "STORE NAME", "sortable": True}
                ]
             },
            {"headerName": "31Q Plan",
                "children": [
                    {"headerName": "Sales Target",
                        "field": "Sales Target", "sortable": True},
                    {"headerName": "Accum Sales",
                        "field": "Accum Sales", "sortable": True,
                        "valueGetter": JsCode("""function(params){
                            if (!params.node.group) {
                                var arr = [];
                                params.data['CY Sales'].forEach(value => {
                                    console.logs("test2", value)
                                });

                                return "test";
                            }
                        }""")
                    }
                ]
             },
            {"headerName": "Actual "+yearCurr,
                "children": [
                    {"headerName": "Sales", "field": "CY Sales",
                        "sortable": True},
                    {"headerName": "Accu Sales",
                        "field": "CY Accu Sales", "sortable": True,},
                    {"headerName": "GC",
                        "field": "CY GC", "sortable": True},
                    {"headerName": "Accu GC", "field": "CY Accu GC",
                        "sortable": True},
                    {"headerName": "AC", "field": "CY AC", "sortable": True,
                     "valueGetter": JsCode("""function(params){
                        if (!params.node.group) {
                            return {
                                "CY Sales":params.data['CY Sales'],
                                "CY GC":params.data['CY GC'],
                                toString: () => params.data['CY AC']
                            };
                        }
                        }""")
                     }
                ]
             },
            {"headerName": "Actual "+yearOld,
                "children": [
                    {"headerName": "Sales", "field": "LY Sales",
                        "sortable": True,},
                    {"headerName": "Accu Sales",
                        "field": "LY Accu Sales", "sortable": True},
                    {"headerName": "GC",
                        "field": "LY GC", "sortable": True},
                    {"headerName": "Accu GC", "field": "LY Accu GC",
                        "sortable": True},
                    {"headerName": "AC", "field": "LY AC", "sortable": True,
                     "valueGetter": JsCode("""function(params){
                        if (!params.node.group) {
                            return {
                                "LY Sales":params.data['LY Sales'],
                                "LY GC":params.data['LY GC'],
                                toString: () => params.data['LY AC']
                            };
                        }
                        }""")
                     }
                ]
             },
            {"headerName": "% Comp. MTD",
                "children": [
                    {"headerName": "Sales",
                        "field": "% Comp. Sales", "sortable": True,
                        "cellClassRules": {
                            'cell-span': "value < 0",
                        },
                     "valueGetter": JsCode("""function(params){
                        if (!params.node.group) {
                            return {
                                "CY Accu Sales":params.data['CY Accu Sales'],
                                "LY Accu Sales":params.data['LY Accu Sales'],
                                toString: () => params.data['% Comp. Sales']
                            };
                        }
                        }""")
                     },
                    {"headerName": "GC",
                        "field": "% Comp. GC", "sortable": True,
                        "cellClassRules": {
                            'cell-span': "value < 0",
                        },
                     "valueGetter": JsCode("""function(params){
                        if (!params.node.group) {
                            return {
                                "CY GC":params.data['CY GC'],
                                "LY GC":params.data['LY GC'],
                                toString: () => params.data['% Comp. GC']
                            };
                        }
                        }""")
                     }
                ]
             },
            {"headerName": "% Achiev",
                "children": [
                    {"headerName": "Sales", "field": "%Achieve Sales", "sortable": True,
                     "cellClassRules": {
                         'cell-span': "value < 0",
                     },
                     "valueGetter": JsCode("""function(params){
                        if (!params.node.group) {
                            return {
                                "Accum Sales":params.data['Accum Sales'],
                                "LY Accu Sales":params.data['LY Accu Sales'],
                                toString: () => params.data['%Achieve Sales']
                            };
                        }
                        }""")
                     }
                ]
             },
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
                                                      """)
                   }

        # df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
        AgGrid(self.resReport, gridOptions=options, allow_unsafe_jscode=True)
