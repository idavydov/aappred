#!/bin/bash
ac=$1

if [ -z "$ac" ]; then
    echo Specify uniprot accession
    exit 4
fi

ffn=$ac.fasta
if fasta=`curl http://www.uniprot.org/uniprot/$ac.fasta --output $ffn`; then
    echo Downloaded fasta: $ffn >&2
else
    echo Error downloading fasta >&2
    exit 1
fi

base=http://www.bioinf.ru
pfn=$ac.dat
if curl $base/aappred/predict --get --data csv=1 --data img=1 --data-urlencode seq@$ffn --output $pfn; then
    echo Got prediction: $pfn >&2
else
    echo Error prediction >&2
    exit 2
fi

cfn=$ac.csv
if grep -v '^#\|^$' $pfn > $cfn; then
    echo Created csv file: $cfn >&2
else
    echo Error creating csv file >&2
fi

images=$(sed -n "/^#img/ s/^#img //p" < $pfn)

ifn=$ac.png
if montage -mode concatenate -tile 1x $images $ifn; then
    echo Created image: $ifn >&2;
else
    echo Error creating image >&2
    exit 3
fi

