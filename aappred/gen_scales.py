#!/usr/local/bin/python
import scales


def calc_2d_val(seq, sca):
	mx=max(sca.values())
	mn=min(sca.values())
	r=0.0
	for i in range(len(seq)-1):
		key=seq[i:i+2]
		if key in sca:
			r+=sca[seq[i:i+2]]
		else:
			r+=0.5 #middle
	r=r/(len(seq)-1)
	return (r-mn)/(mx-mn)

def calc_1d_val(seq, sca):
	mx=max(sca.values())
	mn=min(sca.values())
	r=0.0
	for i in range(len(seq)):
		key=seq[i]
		if key in sca:
			r+=sca[seq[i]]
		else:
			r+=0.5 #middle
	r=r/(len(seq))
	return (r-mn)/(mx-mn)



def upper_list(samples):
	return map(lambda s: s.upper(),samples)

def calc_props(samples):
	scales_1d=[scales.hydro, scales.flexi, scales.acces,
		scales.expos, scales.turns, scales.antig, scales.polar]

	ret_list=[]

	samples=upper_list(samples)
	
	for sample in samples:
		val=[]
		val.append(calc_2d_val(sample,scales.aap))
		for sc in scales_1d:
			val.append(calc_1d_val(sample,sc))
		ret_list.append(tuple(val))
	return ret_list

def calc_prop(samples):
	ret_list=[]
	
	samples=upper_list(samples)

	for sample in samples:
		val=[]
		val.append(calc_2d_val(sample,scales.aap))
		ret_list.append(tuple(val))
	return ret_list

