'''
this sc script is used to upload files to gcp cloud storage.

useful links:

Google github repo
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/storage/cloud-client/storage_upload_file.py

https://cloud.google.com/storage/docs/downloading-objects#storage-download-object-python

'''
import io
import sys
from io import StringIO
from os.path import join

# [START storage_upload_file]
from google.cloud import storage


class GCS:

    @staticmethod
    def upload_blob(bucket_name, src_file_name, tar_blob_name):
        """Uploads a file to the bucket."""
        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(tar_blob_name)
            blob.upload_from_filename(src_file_name)

            # print( "File {} uploaded to {}.".format( src_file_name, tar_blob_name ) )
        except Exception as e:
            print('error uploading {}/{}, src:{}'.format(bucket_name, tar_blob_name, src_file_name))

    @staticmethod
    def upload_blob_from_string(bucket_name, src_string, tar_blob_name):
        try:
            # Get the bucket that the file will be uploaded to.
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)

            # Create a new blob and upload the file's content.
            my_file = bucket.blob(tar_blob_name)

            # create in memory file
            output = io.StringIO(src_string)

            # upload from string
            my_file.upload_from_string(output.read(), content_type="text/plain")
            output.close()

            # list created files
            """ blobs = storage_client.list_blobs(bucket)
            for blob in blobs:
                print(blob.name) """

            # Make the blob publicly viewable.
            # my_file.make_public()

        except Exception as e:
            print('error uploading {}/{}, src_string: {}'.format(bucket_name, tar_blob_name, src_string))

    @staticmethod
    def get_str_from_blob(bucket_name, file_name):
        try:
            # Get the bucket that the file will be uploaded to.
            storage_client = storage.Client()
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob = blob.download_as_string()
            blob = blob.decode('utf-8')
            return blob
        except Exception as e:
            print('qshop.GCS.get_str_from_blob(), error {}'.format(e))

    @staticmethod
    def download_blob(bucket_name, source_blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your GCS object
        # source_blob_name = "storage-object-name"

        # The path to which the file should be downloaded
        # destination_file_name = "local/path/to/file"

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)

        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        # print(
        #    "Downloaded storage object {} from bucket {} to local file {}.".format(
        #        source_blob_name, bucket_name, destination_file_name
        #    )
        # )

    @staticmethod
    def get_file_list(bucket_name, folder_path):

        try:
            '''Take as input bucket and folder, and return a list of strings,
            each element in the list is a file name.
            '''

            storage_client = storage.Client()
            # bucket         = storage_client.get_bucket( bucket_name )
            blobs = storage_client.list_blobs(bucket_name
                                              , prefix=folder_path, delimiter='/')

            # print( 'GCS.get_file_list()... files in folder' )
            # print("Blobs name:")

            a = []
            for blob in blobs:
                # print(blob.name)
                a.append(blob.name)

            # print("Prefixes:")
            # for prefix in blobs.prefixes:
            #    print(prefix)

            return a

        except Exception as e:
            print('qshop.GCS.get_file_list(), error {}'.format(e))

    @staticmethod
    def get_public_url_list(bucket_name, folder_path):

        try:
            '''Take as input bucket and folder, and return a list of strings,
            each element in the list is a file name.
            '''
            storage_client = storage.Client()
            blobs = storage_client.list_blobs(bucket_name, prefix=folder_path, delimiter='/')
            a = []

            # print( 'GCS.get_public_url_list()... files in folder' )
            # print( 'bucket: {}'.format( bucket_name )  )
            # print( 'file_path: {}'.format( folder_path ) )
            # print("Blobs name:")

            for blob in blobs:
                a.append(blob.public_url)
                # print( blob.public_url )

            # print("Prefixes:")
            # for prefix in blobs.prefixes:
            #    print(prefix)

            return a

        except Exception as e:
            print('qshop.GCS.get_public_url_list(), error {}'.format(e))


