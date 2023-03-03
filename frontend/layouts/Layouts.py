from st_aggrid import AgGrid
from layouts.Layouts import *
import streamlit as st
from database.dbConfig import *
from function.cal import *

with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def layout_showUser(user):
    st.markdown("""
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    """, unsafe_allow_html=True)
    return f"""
            <div class="row align-items-center text-secondary">
                <div class="col">Profit name</div>
                <div class="col">Patch name</div>
            </div>
             <div class="row align-items-center font-weight-bold">
                <div class="col">{user[0]}</div>
                <div class="col">{user[1]}</div>
            </div>
            <div class="row align-items-center text-secondary mt-2">
                <div class="col">Store code</div>
                <div class="col">Store name</div>
            </div>
             <div class="row align-items-center font-weight-bold">
                <div class="col">{user[2]}</div>
                <div class="col">{user[3]}</div>
            </div>
    """


def showReport(s_date, e_date):
    # col_btnExport = st.columns(1)
    # with col_btnExport[0]:
    #     # st.session_state.btnE = st.button("Export to Excel")
    #     st.markdown("""
    #                 <script>
    #                     const getParams = () => ({
    #                     processCellCallback(params) {
    #                         const value = params.value;
    #                         return value === undefined ? '' : `_${value}_`;
    #                     },
    #                     processRowGroupCallback(params) {
    #                         const { node } = params;

    #                         if (!node.footer) {
    #                         return `row group: ${node.key}`;
    #                         }
    #                         const isRootLevel = node.level === -1;

    #                         if (isRootLevel) {
    #                         return 'Total';
    #                         }
    #                         return `Sub Total (${node.key})`;
    #                     },
    #                     });

    #                     function onBtExport() {
    #                         gridOptions.api.exportDataAsExcel(getParams());
    #                     }
    #                 </script>
    #                 <button onclick="onBtExport()" style="margin: 5px 0px font-weight: bold">
    #                     Export to Excel
    #                 </button>""", unsafe_allow_html=True)

    yearCurr = str(s_date.year)
    yearOld = str(s_date.year-1)

    sql = "select * from vw_Net_Sales_Report where " + '"Date"' + \
        " between "+f"'{s_date}'" + " and " + f"'{e_date}'"
    result = connectDB(sql)
    # st.write(sql)

    columnDefs = [
        {"headerName": "",
            "children": [
                {"headerName": "Date", "field": "Date",
                    "sortable": True, "aggFunc": JsCode("""function(params) {
                        return "Total Sales";
                    }""")},
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
                    "field": "Sales Target", "sortable": True, "aggFunc": 'sum'},
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
                    }"""),
                    "aggFunc": JsCode("""function(params) {
                            let totalSales = 0;
                            let totalGC = 0;

                            params.values.forEach(value => {
                                if (value && value['CY Sales']) {
                                    totalSales += value['CY Sales'];
                                }
                                if (value && value['CY GC']) {
                                    totalGC += value['CY GC'];
                                }
                            });

                            let sum = 0;
                            sum = totalSales / totalGC;
                            return parseFloat(sum).toFixed(2);
                        }""")},
            ]
         },
        {"headerName": "Actual "+yearCurr,
            "children": [
                {"headerName": "Sales", "field": "CY Sales",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu Sales",
                    "field": "CY Accu Sales", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "GC",
                    "field": "CY GC", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu GC", "field": "CY Accu GC",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "AC", "field": "CY AC", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                    if (!params.node.group) {
                        return {
                            "CY Sales":params.data['CY Sales'],
                            "CY GC":params.data['CY GC'],
                            toString: () => params.data['CY AC']
                        };
                    }
                    }"""),
                 "aggFunc": JsCode("""function(params) {
                        let totalSales = 0;
                        let totalGC = 0;

                        params.values.forEach(value => {
                            if (value && value['CY Sales']) {
                                totalSales += value['CY Sales'];
                            }
                            if (value && value['CY GC']) {
                                totalGC += value['CY GC'];
                            }
                        });

                        let sum = 0;
                        sum = totalSales / totalGC;
                        return parseFloat(sum).toFixed(2);
                    }""")
                 }
            ]
         },
        {"headerName": "Actual "+yearOld,
            "children": [
                {"headerName": "Sales", "field": "LY Sales",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu Sales",
                    "field": "LY Accu Sales", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "GC",
                    "field": "LY GC", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu GC", "field": "LY Accu GC",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "AC", "field": "LY AC", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                    if (!params.node.group) {
                        return {
                            "LY Sales":params.data['LY Sales'],
                            "LY GC":params.data['LY GC'],
                            toString: () => params.data['LY AC']
                        };
                    }
                    }"""),
                 "aggFunc": JsCode("""function(params) {
                        let totalSales = 0;
                        let totalGC = 0;

                        params.values.forEach(value => {
                            if (value && value['LY Sales']) {
                                totalSales += value['LY Sales'];
                            }
                            if (value && value['LY GC']) {
                                totalGC += value['LY GC'];
                            }
                        });

                        let sum = 0;
                        sum = totalSales / totalGC;
                        return parseFloat(sum).toFixed(2);
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
                    }"""),
                 "aggFunc": JsCode("""function(params) {
                        let totalAccCurr = 0;
                        let totalAccOld = 0;

                        params.values.forEach(value => {
                            if (value && value['CY Accu Sales']) {
                                totalAccCurr += value['CY Accu Sales'];
                            }
                            if (value && value['LY Accu Sales']) {
                                totalAccOld += value['LY Accu Sales'];
                            }
                        });

                        let sum = 0;
                        sum = (totalAccOld-totalAccCurr)/totalAccCurr;
                        return sum.toLocaleString(undefined,{style: 'percent'}); ;
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
                    }"""),
                 "aggFunc": JsCode("""function(params) {
                        let totalGCCurr = 0;
                        let totalGCAccOld = 0;

                        params.values.forEach(value => {
                            if (value && value['CY GC']) {
                                totalGCCurr += value['CY GC'];
                            }
                            if (value && value['LY GC']) {
                                totalGCAccOld += value['LY GC'];
                            }
                        });

                        let sum = 0;
                        sum = (totalGCAccOld-totalGCCurr)/totalGCCurr;
                        return sum.toLocaleString(undefined,{style: 'percent'}); ;
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
                    }"""),
                 "aggFunc": JsCode("""function(params) {
                        let totalAcc = 0;
                        let totalAccum = 0;

                        params.values.forEach(value => {
                            if (value && value['Accum Sales']) {
                                totalAccum += value['Accum Sales'];
                            }
                            if (value && value['LY Accu Sales']) {
                                totalAcc+= value['LY Accu Sales'];
                            }
                        });

                        let sum = 0;
                        sum = totalAcc/totalAccum;
                        return sum.toLocaleString(undefined,{style: 'percent'}); ;
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

    css = {
        ".ag-header-group-cell-label": {
            "text-align": "center"
        },
        # ".ag-root-wrapper": {
        #     "border": "none !important",
        #     "border-radius": "10px !important"
        # },
        ".ag-theme-alpine .ag-layout-auto-height .ag-center-cols-clipper, .ag-theme-alpine .ag-layout-auto-height .ag-center-cols-container, .ag-theme-alpine .ag-layout-print .ag-center-cols-clipper, .ag-theme-alpine .ag-layout-print .ag-center-cols-container, .ag-theme-alpine-dark .ag-layout-auto-height .ag-center-cols-clipper, .ag-theme-alpine-dark .ag-layout-auto-height .ag-center-cols-container, .ag-theme-alpine-dark .ag-layout-print .ag-center-cols-clipper, .ag-theme-alpine-dark .ag-layout-print .ag-center-cols-container, .ag-theme-streamlit .ag-layout-auto-height .ag-center-cols-clipper, .ag-theme-streamlit .ag-layout-auto-height .ag-center-cols-container, .ag-theme-streamlit .ag-layout-print .ag-center-cols-clipper, .ag-theme-streamlit .ag-layout-print .ag-center-cols-container, .ag-theme-streamlit-dark .ag-layout-auto-height .ag-center-cols-clipper, .ag-theme-streamlit-dark .ag-layout-auto-height .ag-center-cols-container, .ag-theme-streamlit-dark .ag-layout-print .ag-center-cols-clipper, .ag-theme-streamlit-dark .ag-layout-print .ag-center-cols-container": {
            "min-height": "0 !important"
        },
        ".ag-header-cell-label, .ag-header-group-cell-label": {
            "justify-content": "center"
        },
        ".cell-span": {
            "color": "red"
        }
    }

    AgGrid(result, gridOptions=options, custom_css=(
        css), allow_unsafe_jscode=True)
