
#adconnect.authenticate('LDAP://THBKKDC201.corp.pri:389', 'TH-WFAdmin', 'McThaiJG2018')
# l = authenticate('THBKKDC201.corp.pri:389', 'TH-WFAdmin', 'McThaiJG2018')
#
# import sys, ldap
#
# # DN = username@example.com, secret = password, un = username
# # DN, secret, un = sys.argv[1:4]
# secret = "TH-WFAdmin"
# un = "McThaiJG2018"
#
# server = "ldap://THBKKDC201.corp.pri"
# port = 389
#
# base = "OU=TH-Users,OU=TH,DC=corp,DC=pri"
# scope = ldap.SCOPE_SUBTREE
# filter = "(&(objectClass=user)(sAMAccountName=" + un + "))"
# attrs = ["*"]
#
# l = ldap.initialize(server)
# l.protocol_version = 3
# l.set_option(ldap.OPT_REFERRALS, 0)
#
# # print l.simple_bind_s(DN, secret)
#
# r = l.search(base)
# type, user = l.result(r, 60)
#
# name, attrs = user[0]
#
# if hasattr(attrs, 'has_key') and attrs.has_key('displayName'):
#     print(attrs)
#
# sys.exit()

#pip install ldap3
# ldapsearch -x
# -H ldap://THBKKDC201.corp.pri:389
# -b "CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri"
# -D "CN=TH-WFAdmin,OU=TH-Service Accounts,OU=TH,DC=corp,DC=pri"

from ldap3 import Server, Connection, SAFE_SYNC
server = Server('LDAP://THBKKDC201.corp.pri:389')
conn = Connection(server, 'TH-WFAdmin', 'McThaiJG2018', client_strategy=SAFE_SYNC, auto_bind=True)

# status, result, response, _ = conn.search('CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri', '(&(objectclass=*))', attributes=['member'])
status, result, response, _ = conn.search('CN=TH All_Stores,OU=TH-Distribution Groups,OU=TH,DC=corp,DC=pri', '(&(objectclass=*))', attributes=['member'])

print(status)
print(result)
print(response)
