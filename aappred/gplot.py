import os

def plot(data, mn, mx):
    items=data.split(',')
    plot_data=[]
    for item in items:
        if len(item)!=0:
            plot_data.append(item.split(':'))

    gi,go,ge=os.popen3("/usr/bin/gnuplot")
    gi.write("set output\n")
    gi.write("set term png size 800,300\n")
    gi.write("set xtics 5\n")
    gi.write("""\
    plot [%d:%d] [-3.:+3.] \
'-' title "multi" with lines,\
'-' title "aap" with lines
    """ % (mn,mx))

    for i in plot_data:
        gi.write(str(i[0])+" "+str(i[1])+"\n")
    gi.write("e\n")

    for i in plot_data:
        gi.write(str(i[0])+" "+str(i[2])+"\n")
    gi.write("e\n")

    gi.write("e\n")
    gi.close()

    out = go.read()
    
    go.close()

    return out
