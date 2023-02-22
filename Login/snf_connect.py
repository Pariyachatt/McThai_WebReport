import streamlit as st
from database.dbConfig import *


sql = "select * from vw_Net_Sales_Report where " + '"Date"' + \
    " between "+f"'{s_date}'" + " and " + f"'{e_date}'"
result = connectDB(sql)

print(result)
