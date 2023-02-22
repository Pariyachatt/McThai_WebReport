
#adconnect.authenticate('LDAP://THBKKDC201.corp.pri:389', 'TH-WFAdmin', 'McThaiJG2018')
# l = authenticate('THBKKDC201.corp.pri:389', 'TH-WFAdmin', 'McThaiJG2018')

import sys, ldap

# DN = username@example.com, secret = password, un = username
# DN, secret, un = sys.argv[1:4]
secret = "TH-WFAdmin"
un = "McThaiJG2018"

server = "ldap://THBKKDC201.corp.pri"
port = 389

base = "OU=TH-Users,OU=TH,DC=corp,DC=pri"
scope = ldap.SCOPE_SUBTREE
filter = "(&(objectClass=user)(sAMAccountName=" + un + "))"
attrs = ["*"]

l = ldap.initialize(server)
l.protocol_version = 3
l.set_option(ldap.OPT_REFERRALS, 0)

# print l.simple_bind_s(DN, secret)

r = l.search(base)
type, user = l.result(r, 60)

name, attrs = user[0]

if hasattr(attrs, 'has_key') and attrs.has_key('displayName'):
    print attrs

sys.exit()
