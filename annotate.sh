#!/bin/bash

for d in $@ ; do 
	echo $d;
	for f in ${d}/*EEDP*png; do
		convert -background '#0008' -fill white -gravity center -size 2048x30 caption:"$d" $f +swap -gravity north -composite  $f;
	done;
done
