# 题目：写一个能跑起来的单页网页，验证“Python 脚本 = 网页”这个概念。
# 要求包含：
# 一个大标题（st.title）和一段介绍文字（st.write，它什么都能显示：文字、数字、变量）
# 一个交互组件自选其一：按钮（st.button）、滑块（st.slider）、文本输入框（st.text_input）——选一个就好，感受“我动了它 → 页面变了”
# 用滑块或输入框的值实时显示点什么（比如滑块选 1-100，页面显示“你选了 37”）
import streamlit as st
st.title("Hello Streamlit")
st.write("这是一个简单的 Streamlit 网页示例，展示了如何将 Python 脚本转换为网页应用。你可以通过交互组件来改变页面内容。")
# 滑动选择数字
number = st.slider("请选择一个数字", 1, 100)
st.write("你选择的数字是：", number)
# 输入文本
name = st.text_input("请输入你的名字")
if name:
    st.write(f"你好，{name}！欢迎使用 Streamlit。")
    st.button("点击我")
gender = st.radio("请选择你的性别",["男","女"])
st.write(f"你的性别是：{gender}")                  
                  