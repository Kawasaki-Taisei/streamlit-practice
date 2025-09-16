import streamlit as st

st.title("High and Low Game!")

import streamlit as st
import random

# --------------------------
# 初期化
# --------------------------
if "current" not in st.session_state:
    st.session_state.current = random.randint(1, 13)
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🎲 ハイアンドロー（数字版）")

# 現在のカード
st.subheader(f"現在の数字: {st.session_state.current}")

# ボタンで予想
col1, col2 = st.columns(2)

def play(guess: str):
    next_num = random.randint(1, 13)
    result = None
    if next_num == st.session_state.current:
        result = "引き分け"
    elif guess == "high" and next_num > st.session_state.current:
        st.session_state.score += 1
        result = "正解！"
    elif guess == "low" and next_num < st.session_state.current:
        st.session_state.score += 1
        result = "正解！"
    else:
        result = "不正解…"

    st.session_state.current = next_num
    st.session_state.result = f"次の数字: {next_num} → {result}"

with col1:
    if st.button("⬆️ High"):
        play("high")
with col2:
    if st.button("⬇️ Low"):
        play("low")

# 結果表示
if "result" in st.session_state:
    st.write(st.session_state.result)

st.metric("スコア", st.session_state.score)

# リセットボタン
if st.button("🔄 リセット"):
    st.session_state.current = random.randint(1, 13)
    st.session_state.score = 0
    st.session_state.result = "リセットしました"
