from pysnmp.hlapi import *
engine = SnmpEngine()
community = CommunityData('novecerchi', mpModel=1)
transport = UdpTransportTarget(('192.168.1.175', 161))
context = ContextData()


TURN_ON_TRIPPLITE = '.1.3.6.1.4.1.850.1.1.3.5.4.1.1.2.1'
TURN_OFF_TRIPLITE = '.1.3.6.1.4.1.850.1.1.3.5.4.1.1.3.1'

# Your OID goes here.
identity = ObjectIdentity( TURN_ON_TRIPPLITE )

# If this was a string value, use OctetString() instead of Integer().
new_value = Integer(1)
t = ObjectType(identity, new_value)

try:
	# Setting lookupMib=False here because this example uses a numeric OID.
	g = setCmd(engine, community, transport, context, t, lookupMib=False)

	errorIndication, errorStatus, errorIndex, varBinds = next(g)
	print(errorIndication, varBinds)
except:
    pass
