import streamlit as st
import numpy as np
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance,get_face_embeddings,train_classifier
import time
from src.database.db import get_all_students,create_student
from src.pipelines.voice_pipeline import get_voice_embedding

from PIL import Image

def student_dashboard():
    st.header("Student Dashboard",text_alignment="center")

def student_screen():

    style_background_dashboard()
    style_base_layout()
    if "student_data" in st.session_state:
        student_dashboard()
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

        st.header("Login using face ID",text_alignment="center")
        st.space()
        st.space()
        show_registeration = False

        photo_source =st.camera_input("Position your face in the camera")
        if photo_source:
            img = np.array(Image.open(photo_source))
            with st.spinner("AI is scanning your face..."):
                detected ,all_ids,num_faces = predict_attendance(img)

                if num_faces == 0 :
                    st.error("No face detected")
                elif num_faces > 1:
                    st.error("Multiple faces detected")
                else:
                    if detected:
                        student_id = list(detected.keys())[0]
                        all_students = get_all_students()
                        student = next((s for s in all_students if s['student_id'] == student_id),None)
                        if student:
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = "student"
                            st.session_state.student_data = student
                            st.toast(f"welcome back{student['name']}")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.info("Student face not recognized! you might be a new student")
                        show_registeration = True
        if show_registeration:
            with st.container(border=True):
                st.header("Register as a new student",text_alignment="center")
                new_name = st.text_input("Enter your name")
                st.subheader("Optional: voice Enrollment")
                st.info("Enroll for voice only attendance")
                audio_data = None

                try:
                    audio_data = st.audio_input("Record a short phrase like I am present,my name is "+new_name)
                except Exception as e:
                    st.error("Audio Datafailed")
                
                if st.button("Create Account",type="primary"):
                    if new_name :
                        with st.spinner("Creating your profile..."):
                            img = np.array(Image.open(photo_source))
                            encodings = get_face_embeddings(img)
                            if encodings:
                                face_emb = encodings[0].tolist()
                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())
                                
                                response_data = create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)
                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = "student"
                                    st.session_state.student_data = response_data[0]
                                    st.toast(f"new student {response_data[0]['name']}")
                                    time.sleep(1)
                                    st.rerun()
                                else :
                                    st.error("Failed to capture your face")


                    else:
                        st.warning("Please enter your name")
        footer_dashboard()
