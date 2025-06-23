from get_receipt import find_receipt
from datetime import datetime
r=find_receipt(0x07cdcf91340405aa80106c7f0cd4a7602caec453d82e943fcf1669699515c2f7)
#r1=find_receipt(0x497ed7f84a69f15bdbe7d73bf72da57255af9402ab24bb586368e0d328eae851)
#r2=find_receipt(0x781f26dffc7ed86e20c43a6b52a430a07472380a55bed9fb3af980621d390572)

print(r['status'])

status=r['status']

if status == 1:
 print('transaction successful')
elif statuss == 0:
 print('transaction failed')
 
now=datetime.now()
Time=now.strftime('%Y%m%d%H%M%S') 
print(Time)
