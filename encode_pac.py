import base64
fout = open('./modify_gflist.txt','w')
with open('./newgflist.txt','rb') as f:
    ct = f.read()
    de = base64.b64encode(ct).decode('ascii')
    fout.write(de)
    fout.close()    