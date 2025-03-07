import streamlit as st
import pandas as pd
table = pd.DataFrame({"Column 1 ": [1,2,3,4,5,6,7] , "Column 2" : [11,22,33,44,55,66,77] })
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
st.title("Hi  I am a steamlit web app")
st.header("Nan Dhan da leo")
st.subheader("Dhathooraa")
st.text("inga vanthu text ellam eluthanum like paragraph tag")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("I am a caption this is the caption part ")
st.latex(r"\begin{pmatrix}a&b&90\\c&d&u\end{pmatrix}")
st.markdown("---")
json = {"a":"1,2,3", "b":"4,5,6"}
st.json(json)
st.markdown("---")
code= """
print("hello world)
def func():
    return 0; """
st.code(code , language = "python")
st.markdown("---")
st.write("## nanga dhan")
st.markdown("---")
st.metric(label = "Sarakku", value = "500kgm⁻¹", delta = "-43kgm⁻²³")
st.table(table)
st.markdown("---")
st.dataframe(table)
st.markdown("---") 
st.image("rinnegan.jpg", caption = "I AM THE GHOST OF UCHIHA", width=700)
st.audio("madara_smile.mp3")
st.video("download.mp4") 
def change():
    print(st.session_state.checker)
state = st.checkbox("checker",value=True, on_change=change,key="Checker")     




