import streamlit as st
import tempfile
from st_files_connection import FilesConnection

class AmazonS3Uploader:
    def __init__(self):
        st.title("Upload Files to Amazon S3")
        self.s3_client = FilesConnection('s3')

    def load_credentials(self):
        self.s3_client.set_credentials()

    def upload_file(self, bucket_name, uploaded_file):
        if self.s3_client is not None:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())

            blob_name = uploaded_file.name
            bucket = self.s3_client.bucket(bucket_name)
            blob = bucket.blob(blob_name)

            if blob.exists():
                st.warning("The file already exists. Do you want to replace it?")
                replace_existing = st.button("Replace")
                cancel_upload = st.button("Cancel")

                if replace_existing:
                    try:
                        blob.upload_from_filename(temp_file.name)
                        st.success("Upload to Amazon S3 completed successfully!")
                    except Exception as e:
                        st.error(e)
                elif cancel_upload:
                    st.warning("Upload to Amazon S3 canceled. The existing file will not be replaced.")
            else:
                try:
                    blob.upload_from_filename(temp_file.name)
                    st.success("Upload to Amazon S3 completed successfully!")
                except Exception as e:
                    st.error(e)
        else:
            st.error("Error: Amazon S3 credentials not loaded")