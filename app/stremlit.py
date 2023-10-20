import streamlit as st

from Uploader import AmazonS3Uploader

from TypeFile import UploadAnyFile
from TypeFile import UploadCSV


def main():

    selected_bucket = st.sidebar.selectbox("Selecione o arquivo:", ["Frota", "Monitoramento", "Bilhetagem"])
        
    selected_tab = st.sidebar.selectbox("Select a tab:", ["Upload CSV"])

    selected_cloud = st.sidebar.selectbox("Selecione o servidor:", ["AWS"])

    if selected_cloud == "AWS":
        uploader = AmazonS3Uploader()

    if selected_tab == "Upload CSV":
        UploadCSV(uploader)

if __name__ == "__main__":
    main()