import streamlit as st
from src.database.db import create_subject



@st.dialog("Create New Subjects")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Enter subject id",placeholder="Enter subject id")
    sub_name = st.text_input("Enter subject name",placeholder="Enter subject name")
    sub_section = st.text_input("Enter subject section",placeholder="Enter subject section")


    if st.button("Create Subject Now",type="primary",width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject Create Successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Subject Create Failed: {str(e)}")
        else:
            st.warning("All fields are required!")

