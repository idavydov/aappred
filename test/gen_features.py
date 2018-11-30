#!/usr/bin/env python
import sys
import fasta
import gen_scales


window=20
step=1


record=fasta.fasta(filename=sys.argv[1])

parts=record.split(window, step)

props=gen_scales.calc_props(parts)

for prop in props:
    print ' '.join([str(v) for v in prop])
