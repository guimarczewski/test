import streamlit as st
import pandas as pd
import boto3

from ApplyTests import aplicar_verificacoes

class UploadCSV:
    def __init__(self, uploader, selected_bucket):
        self.uploader = uploader
        aws_access_key_id_input = st.text_input("AWS Access Key ID")
        aws_secret_access_key_input = st.text_input("AWS Secret Access Key", type="password")
        bucket_name = selected_bucket
        uploaded_file = st.file_uploader("Upload CSV file")

        if uploaded_file:
            error_type = aplicar_verificacoes(bucket_name, uploaded_file)
            if error_type is not True:
                self.show_error_message(error_type)
            else:
                if st.button("Upload"):
                    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id_input, aws_secret_access_key=aws_secret_access_key_input)
                    s3.Object(bucket_name, uploaded_file.name).put(Body=uploaded_file.read())