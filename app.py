import streamlit as st

# 入力欄を2つ用意（初期値は0）
num1 = st.number_input("1つ目の数字を入力してください", value=0)
num2 = st.number_input("2つ目の数字を入力してください", value=0)

# 計算結果（ここでは足し算）
result = num1 + num2

# 結果を表示
st.write("計算結果:", result)