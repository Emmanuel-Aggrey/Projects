
import json
import requests
import csv
import pandas  as pd
import pickle
def save_clients(identifier,message):
   

    with open ('clients_ids.csv', 'a') as clients_ids:
        clients  = csv.writer(clients_ids)
        clients.writerow([identifier,message])
        return clients

# CONVERT LIST TO DICT
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    
    return res_dct

# CHECK IF CLIENT HAVE CONNECTED BEFORE
def check_client_availability(available):

    df = pd.read_csv('clients_ids.csv')
    data = [df.to_string(index=False)]
    clean_data= ''.join(data).split()
    if available in clean_data:
        # print('True ',available)
        return True
    else:
        # print('False ',available)
        return False

check_client_availability("9001")




def get_client_unique_id(client_id):
    df = pd.read_csv('clients_ids.csv')
    data = [df.to_string(index=False)]
    clean_data= ''.join(data).split()
    
    client_id = Convert(clean_data).get(client_id,None)
    if client_id:
        print(client_id)
        return client_id
    else: 
        print(client_id)
        return client_id
    # print(data)




get_client_unique_id("9001")

