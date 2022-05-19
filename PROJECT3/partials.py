
import json
import requests
import csv
import pandas  as pd
import os

def save_clients(identifier,message):
   

    with open ('clients_ids.csv', 'a') as clients_ids:
        clients  = csv.writer(clients_ids)
        clients.writerow([identifier,message])
        return clients

# CONVERT LIST TO DICT
def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    
    return res_dct

# CHECK IF CLIENT VALUE EXISTS IN THE LIST
def check_availability(element,collection:iter):
    return element in collection


# CHECK IF FILE EXIST
def check_file_exists():
    file_exist = os.path.isfile('clients_ids.csv')
    if not file_exist:
        with open('clients_ids.csv','x') as csv_file:
            pass
    return True

# CHECK IF CLIENT HAVE CONNECTED BEFORE
def check_client_availability(available):
    df = pd.read_csv('clients_ids.csv',index_col=None)
    
    data = df.to_string(index=False)
    clean_data  = data.split()
    new_dict = convert(clean_data)
    if available in new_dict.keys():
        return True
    else:
        return False

    

# GET UNIQUE CODE FROM SERVER IF CLIENT SENDS ITS IDENTIFIER

def get_client_unique_id(client_id):
        df = pd.read_csv('clients_ids.csv')

        data = df.to_string(index=False)
        clean_data  = data.split()
        new_dict = convert(clean_data).get(client_id,None)


        return new_dict





