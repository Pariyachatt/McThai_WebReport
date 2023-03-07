
"""
How to testing:
step 1:
    ssh root@10.252.179.145

step 2:
ldapsearch -x -b "CN=TH OPS WebReport,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri" -H ldap://THBKKDC201.corp.pri:389 -D "CN=TH-WFAdmin,OU=TH-Service Accounts,OU=TH,DC=corp,DC=pri" -W


ldapsearch -x -b "CN=TH OPS WebReport,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri" -H ldap://THBKKDC201.corp.pri:389 -D "CN=TH-WFAdmin,OU=TH-Service Accounts,OU=TH,DC=corp,DC=pri"  - "(CN=Prachaya Borisuth)" -W

ldapsearch -x -b "CN=TH OPS WebReport,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri" "(objectclass=*)" member CN=Prachaya Borisuth, -H ldap://THBKKDC201.corp.pri:389 -D "CN=TH-WFAdmin,OU=TH-Service Accounts,OU=TH,DC=corp,DC=pri" -W

"""

#pip install ldap3
# ldapsearch -x
# -H ldap://THBKKDC201.corp.pri:389
# -b "CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri"
# -D "CN=TH-WFAdmin,OU=TH-Service Accounts,OU=TH,DC=corp,DC=pri"

from ldap3 import Server, Connection, SAFE_SYNC
server = Server('LDAP://THBKKDC201.corp.pri:389')
conn = Connection(server, 'TH-WFAdmin', 'McThaiJG2018', client_strategy=SAFE_SYNC, auto_bind=True)

# status, result, response, _ = conn.search('CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri', '(&(objectclass=*))', attributes=['member'])
# status, result, response, _ = conn.search('CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri', '(&(objectclass=*))', attributes=['member'])

status, result, response, _ = conn.search('CN=TH OPS WebReport,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri', '(&(objectclass=*))', attributes=['member'])

print(status)
print(result)
print(response)
# print(response['raw_attributes'])
