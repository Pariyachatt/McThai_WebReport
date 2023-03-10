from st_aggrid import AgGrid
from layouts.Layouts import *
import streamlit as st
from database.dbConfig import *
from function.cal import *

def showReport(s_date, e_date):

    yearCurr = str(s_date.year)
    yearOld = str(s_date.year-1)

    sql = "select * from vw_Net_Sales_Report where " + '"Date"' + \
        " between "+f"'{s_date}'" + " and " + f"'{e_date}'"
    result = connectDB(sql)
    # st.write(sql)

    columnDefs = [
        {"headerName": "",
            "children": [
                {
                    "headerName": "Date",
                    "field": "Date",
                    "sortable": True
                },
                {"headerName": "Day", "field": "Day",
                    "sortable": True},
                {"headerName": "Profit name",
                    "field": "PROFIT_NAME", "sortable": True},
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
                    }""")},
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

    AgGrid(result, gridOptions=options, allow_unsafe_jscode=True)
