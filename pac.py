import base64
fout = open('./newgflist.txt','w')
with open('./gfwlist.txt','rb') as f:
    ct = f.read()
    de = base64.b64decode(ct).decode('ascii')
    print(type(de))
    fout.write(de)
    fout.close()    