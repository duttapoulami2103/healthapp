import streamlit as st
st.title("This is my first web application in python")
st.header("I will try my best to learn python")
st.subheader("This is my first attempt to create web application")
st.write("Hello everyone!")
st.markdown("** initial assessment")
st.markdown("## initial project")

if st.button("Say hello, when clicked"):
    st.write("hello")

if st.checkbox("show text"):
        st.write("This text is visible")

choice=st.radio("pick one", ["A","B","C"])
st.write(f"you picked {choice}")

option=st.selectbox("pick one",["X","Y","Z"])
st.write(f"you picked {option}")

level=st.slider("select a value",1,100)
st.write(f"your age is: {level}")

name=st.text_input("what is your name?")
st.write(f"Hello, {name}")

height=st.number_input("what is your heigh in m?")
st.write(f"hello your height is: {height}")

