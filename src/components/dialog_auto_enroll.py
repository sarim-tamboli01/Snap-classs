import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Auto enroll in subject")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id,name').eq('subject_code',subject_code).execute()
    if not res.data:
        st.error('subject code not foound')
        if st.button('close'):
            st.query_params.clear()
            st.rerun()

        return
    subject = res.data[0]

    chack = supabase.table('subject_students').select('*').eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()
    if chack.data:
        st.info('youre already enrolled')
        if st.button('got it!'):
            st.query_params.clear()
            st.rerun()
        return
    st.markdown(f"would you like to enroll in this subject {subject['name']}?")

    c1,c2 = st.columns(2)
    with c1:
        if st.button('No Thanks'):
            st.query_params.clear()
            st.rerun()
    with c2:
        if st.button('Yes Please',type="primary"):
            enroll_student_to_subject(student_id,subject['subject_id'])
            st.success('You have successfully enrolled in this program')
            st.query_params.clear()
            time.sleep(1)
            st.rerun()

