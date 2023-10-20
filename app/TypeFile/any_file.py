import streamlit as st
import boto3

class UploadAnyFile:
    def __init__(self, uploader, selected_bucket):
        self.uploader = uploader
        aws_access_key_id_input = st.text_input("AWS Access Key ID")
        aws_secret_access_key_input = st.text_input("AWS Secret Access Key", type="password")
        bucket_name = selected_bucket
        uploaded_file = st.file_uploader("Upload any file")

        if uploaded_file:
            if st.button("Upload"):
                s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id_input, aws_secret_access_key=aws_secret_access_key_input)
                s3.Object(bucket_name, uploaded_file.name).put(Body=uploaded_file.read())