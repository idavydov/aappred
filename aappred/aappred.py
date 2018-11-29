#!/usr/bin/env python
import web

render = web.template.render('templates/', base='layout')
render_plain = web.template.render('templates/')

import fasta
import sk_predict
import gen_scales
import gplot

window=20
step=1
bigstep=100

def do_predict(samples, many=True, rnd=5):
    if many:
        props = gen_scales.calc_props(samples)
        pred = sk_predict.predict(props, model=sk_predict.props)
    else:
        props = gen_scales.calc_prop(samples)
        pred = sk_predict.predict(props, model=sk_predict.aap)
    if rnd is not None:
        return [round(v, rnd) for v in pred]
    return pred

def plot_data(pr1, pr2):
    subplots = []
    for i in xrange(0,len(pr1),bigstep):
        sdata=""
        for j in xrange(i,min(len(pr1),i+bigstep+1)):
            sdata+="%d:%f:%f,"%((j*step+window/2),pr1[j],pr2[j])
        subplots.append((i+window/2,i+window/2+bigstep,sdata))
    return subplots

class index:
    def GET(self):
        return render.main()

class predict_redirect:
    def GET(self):
        raise web.seeother('/aappred/predict')

class predict:
    def GET(self):
        inp = web.input(seq=None, csv=None, img=None)
        if inp.seq is None:
            return render.form()

        f=fasta.fasta(string=inp.seq)
        parts=f.split(window,step)
        pr1=do_predict(parts,many=True)
        pr2=do_predict(parts,many=False)
        data = []
        for i in xrange(len(pr1)):
            data.append(((i*step+window/2),
                         f.sequence[i*step+window/2].upper(),
                         pr1[i],
                         pr2[i]))

        if inp.csv is None:
            return render.predict(data, inp.seq)
        else:
            return render_plain.predict_csv(data, plot_data(pr1, pr2) if not inp.img is None else None)

class plot:
    def GET(self):
        i = web.input()
        pdata = gplot.plot(i.data, int(i.mn), int(i.mx))
        web.header('Content-Type', 'image/png')
        return pdata

urls = (
    '/aappred/', 'index',
    '/aappred/predict.py', 'predict_redirect',
    '/aappred/predict', 'predict',
    '/aappred/plot', 'plot',
)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
