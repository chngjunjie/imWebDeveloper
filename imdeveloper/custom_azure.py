from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'resumeweb' # Must be replaced by your <storage_account_name>
    account_key = '54HkKXrId6LfAlJD0V/MtMR5YNJX21QsY/OITuBDplKOIvVKLU+W9ttsczwom41DnJN5GR7sBYfmZZaOlSBHHQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None
    file_overwrite = False

class AzureStaticStorage(AzureStorage):
    account_name = 'resumeweb' # Must be replaced by your storage_account_name
    account_key = '54HkKXrId6LfAlJD0V/MtMR5YNJX21QsY/OITuBDplKOIvVKLU+W9ttsczwom41DnJN5GR7sBYfmZZaOlSBHHQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

# file: ./custom_storage/custom_azure.py
class PublicAzureStorage(AzureStorage):
    account_name = 'resumeweb' # Must be replaced by your storage_account_name
    account_key = '54HkKXrId6LfAlJD0V/MtMR5YNJX21QsY/OITuBDplKOIvVKLU+W9ttsczwom41DnJN5GR7sBYfmZZaOlSBHHQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
