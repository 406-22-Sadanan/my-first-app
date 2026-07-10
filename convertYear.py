import streamlit as st
st.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")
bh_yea=st.number_input("กรอกปี พ.ศ.ที่ต้องการแปลง",value=2569)
ce_year=bh_year-543
st.header(f"ปี พ.ศ. คือ : {ce_year}")
