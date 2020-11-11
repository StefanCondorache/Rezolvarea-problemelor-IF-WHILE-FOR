m=int(input("m="))
n=int(input("n="))
putere=0
da=''
nu=''
if m<n:
  for x in range(1,n):
    putere=m**x
    if putere==n:
      da='Da'
    else:
      nu='Nu'
  if da=='Da':
    print(da)
  else:
    print('Nu')
