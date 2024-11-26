import streamlit as st 
import math

st.title(" Menghitung Tabung  :red[Valume tabung] :smile:")
r = st.number_input("masukan jari-jari :",0)
t = st.number_input("masukan tinggi ;",0)
if st.button("volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f"volume tabung adalah {v :.2f}")
   
