
def make_receipt(data,out_file_name):
    f=open(out_file_name,"w")
    f.write((" "*26)+"Name"+(" "*26)+"Item Cost  Tax\n")
    for i in data:
        towrite=""
        towrite+=f"{i[0]}{(" "*(56-len(i[0])))}"
        if i[1]!=None:
            towrite+="${:,.2f}".format(i[1])+(" "*5)
        else:
            towrite+=" "*10
        if i[2]!=None:
            if isinstance(i[2],float) or isinstance(i[2],int):
                towrite+="${:,.2f}".format(i[2])
            else:
                towrite+=i[2]
        towrite+="\n"
        f.write(towrite)
                
    f.close()