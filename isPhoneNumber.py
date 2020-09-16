import re

phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')

mo = phoneNumRegex.search('this string has my num (503)-312-7679')

print(f'phone number is {mo.group()}')

print(f'mo.group(1) : {mo.group(1)}')

print(f'mo.group(2) : {mo.group(2)}')

print(f'mo.group(0) : {mo.group(0)}')

print(f'mo.groups() : {mo.groups()}')

areaCode, mainNumber = mo.groups()

print(f'areaCode : {areaCode}')

print(f'mainNumber : {mainNumber}')

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

bo = batRegex.search('The Batmobile lost a wheel!')
print(bo.group())
print(bo.group(1))

batWoRegex = re.compile(r'Bat(wo)?man')

bw = batWoRegex.search('Batman is here')
bw1 = batWoRegex.search('Batwoman is here')

print(f'bw : {bw.group()} bw1 : {bw1.group()}')

phoneRegOpt = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

po = phoneRegOpt.search('check out 50-312-7679')
print(f'po : {po.group()}')

phoneRegFA = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
fao = phoneRegFA.findall('c: 503-312-7679 o: 897-990-6789')
print(f'fao : {fao}')