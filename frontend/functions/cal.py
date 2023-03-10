from st_aggrid import JsCode
import streamlit as st

with open('./css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def achive(result):
    # for value in result[""'Sales Target'""]:
    #     total += value

    # return result["Sales Target"]

    return JsCode("""function calAchive({result}) {
            return  result
        }""")


def valueGetter():
    return JsCode("""
    function ratioAggFunc(params) {
        let goldSum = 0;
        let silverSum = 0;
        params.values.forEach((value) => {
            if (value && value.gold) {
            goldSum += value.gold;
            }
            if (value && value.silver) {
            silverSum += value.silver;
            }
        });
        return createValueObject(goldSum, silverSum);
    }

    function createValueObject(gold, silver) {
        return {
            gold: gold,
            silver: silver,
            toString: () => `${gold && silver ? gold / silver : 0}`,
        };
    }
    """)


# def calTotal():
#     return JsCode(f"""function (params) {
#         return }""")
