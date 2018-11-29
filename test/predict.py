#!/usr/bin/env python

import sys
import fasta
import gen_scales
import sk_predict

def prediction_print(record, v1, v2):
    assert len(v1) == len(v2)
    for i in xrange(len(v1)):
        print '%d\t%s\t%f\t%f' % (
            (i*step+window/2),
            record.sequence[i*step+window/2].upper(),
            v1[i],
            v2[i])

window=20
step=1

record=fasta.fasta(filename=sys.argv[1])

parts=record.split(window, step)

props1=gen_scales.calc_props(parts)
props2=gen_scales.calc_prop(parts)

pr1 = sk_predict.predict(props1,sk_predict.props)
pr2 = sk_predict.predict(props2,sk_predict.aap)

prediction_print(record, pr1, pr2)
