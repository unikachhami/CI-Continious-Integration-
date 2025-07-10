import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate it square cube and fifth power:")

n = st.number_input("Enter an integer",value=1,step=1)

square = n**2
cube = n**3
fifth = n**5

st.write(f"Square of {n}is",(square))
st.write(f"Cube of {n}is",(cube))
st.write(f"Fifth power of {n}is",(fifth))

