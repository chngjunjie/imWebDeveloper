from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'allenchngstorage' # Must be replaced by your <storage_account_name>
    account_key = 'OPN6jIFVQq9zl0/NPYWFGt1OveWBrMRWosSaBG7uovto55rJ7mY+HzBstLsQfWOiHESpGigZWifiH+n5D6l8iA==' # Must be replaced by your <storage_account_key>
    azure_container = 'lavamedia'
    expiration_secs = None
    file_overwrite = False

class AzureStaticStorage(AzureStorage):
    account_name = 'allenchngstorage' # Must be replaced by your storage_account_name
    account_key = 'OPN6jIFVQq9zl0/NPYWFGt1OveWBrMRWosSaBG7uovto55rJ7mY+HzBstLsQfWOiHESpGigZWifiH+n5D6l8iA==' # Must be replaced by your <storage_account_key>
    azure_container = 'lavastatic'
    expiration_secs = None

# file: ./custom_storage/custom_azure.py
class PublicAzureStorage(AzureStorage):
    account_name = 'allenchngstorage' # Must be replaced by your storage_account_name
    account_key = 'OPN6jIFVQq9zl0/NPYWFGt1OveWBrMRWosSaBG7uovto55rJ7mY+HzBstLsQfWOiHESpGigZWifiH+n5D6l8iA==' # Must be replaced by your <storage_account_key>
    azure_container = 'lavastatic'
    expiration_secs = None
