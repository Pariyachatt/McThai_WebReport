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
    col_btnExport = st.columns(1)
    with col_btnExport[0]:
        st.session_state.btnE = st.button("Export to Excel")

    yearCurr = str(s_date.year)
    yearOld = str(s_date.year-1)

    # sql = f"select * from vw_net_sales_report where ""'Start Date'"" between '{s_date}' and '{e_date}'"
    sql = "select * from vw_net_sales_report"
    result = connectDB(sql)

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
                    "field": "Profit Name", "sortable": True},
                {"headerName": "Patch name", "field": "Patch Name", "sortable": True},
                {"headerName": "Store code", "field": "Store Code", "sortable": True}
            ]
         },
        {"headerName": "31Q Plan",

            "children": [
                {"headerName": "Sales Target",
                    "field": "Sales Target", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accum Sales",
                    "field": "Accum Sales", "sortable": True,
                    "aggFunc": 'sum'},
            ]
         },
        {"headerName": "Actual "+yearCurr,
            "children": [
                {"headerName": "Sales", "field": "TY Sales",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu Sales",
                    "field": "TY Accu Sales", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "GC",
                    "field": "TY GC", "sortable": True, "aggFunc": 'sum'},
                {"headerName": "Accu GC", "field": "TY Accu GC",
                    "sortable": True, "aggFunc": 'sum'},
                {"headerName": "AC", "field": "TY AC", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                     console.log('test',params.node);
                    if (!params.node.group) {
                        return {
                            "TY Sales":params.data['TY Sales'],
                            "TY GC":params.data['TY GC'],
                            toString: () => params.data['TY AC']
                        };
                    }
                    }"""),
                 "aggFunc": JsCode("""function(params) { 
                        let totalSales = 0;
                        let totalGC = 0;
                                            
                        params.values.forEach(value => {
                            if (value && value['TY Sales']) {
                                totalSales += value['TY Sales'];
                            }
                            if (value && value['TY GC']) {
                                totalGC += value['TY GC'];
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
                    "field": "CompMTDSales", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                    if (!params.node.group) {
                        return {
                            "TY Accu Sales":params.data['TY Accu Sales'],
                            "LY Accu Sales":params.data['LY Accu Sales'],
                            toString: () => params.data['CompMTDSales']
                        };
                    }
                    }"""),
                 "aggFunc": JsCode("""function(params) { 
                        let totalAccCurr = 0;
                        let totalAccOld = 0;
                                            
                        params.values.forEach(value => {
                            if (value && value['TY Accu Sales']) {
                                totalAccCurr += value['TY Accu Sales'];
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
                    "field": "CompMTDGC", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                    if (!params.node.group) {
                        return {
                            "TY GC":params.data['TY GC'],
                            "LY GC":params.data['LY GC'],
                            toString: () => params.data['CompMTDGC']
                        };
                    }
                    }"""),
                 "aggFunc": JsCode("""function(params) { 
                        let totalGCCurr = 0;
                        let totalGCAccOld = 0;
                                            
                        params.values.forEach(value => {
                            if (value && value['TY GC']) {
                                totalGCCurr += value['TY GC'];
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
                {"headerName": "Sales", "field": "% Achiev Sales", "sortable": True,
                 "valueGetter": JsCode("""function(params){
                    if (!params.node.group) {
                        return {
                            "Accum Sales":params.data['Accum Sales'],
                            "LY Accu Sales":params.data['LY Accu Sales'],
                            toString: () => params.data['% Achiev Sales']
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
               "api": "exportDataAsExcel()"
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
        }
    }

    AgGrid(result, gridOptions=options, custom_css=(
        css), allow_unsafe_jscode=True)
