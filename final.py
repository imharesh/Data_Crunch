import pandas as pd

f_1 = pd.read_csv('ip_1m.tsv', sep= '\t', low_memory=False)
f_2 = pd.read_csv('user_email_hash.1m.tsv', sep= '\t')
f_3 = pd.read_csv('plain_32m.tsv', sep= '\t')

create_dict = {'ID':f_2['id'],
               'USERNAME':f_2['username'],
               'EMAIL':f_2['email'],
               'HASH_PASS':f_2['password'], 
               'PLAIN_PASS':f_3.iloc[:,1],
               'IP':f_1['ip_address']}

df =pd.DataFrame(create_dict)
df.to_csv('final_dict', sep="\t")



 