TMPDIR=/tmp
for lang in br ca cy de fr kab ky ; do
	if [[ ! -d ../$lang ]]; then
		continue	
	fi
	echo $lang
	echo -n "" > $TMPDIR/$lang.dat
	wer_baseline=$(cat ../$lang/LOG.$lang.scratch | grep 'Test - ' | grep -o 'WER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g'); 
	cer_baseline=$(cat ../$lang/LOG.$lang.scratch | grep 'Test - ' | grep -o 'CER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g');
	for model in 1 2 3 4 5; do
		wer=$(cat ../$lang/LOG.$lang.$model | grep 'Test - ' | grep -o 'WER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g');
		cer=$(cat ../$lang/LOG.$lang.$model | grep 'Test - ' | grep -o 'CER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g');

		echo -e "$lang\t$model\t$wer\t$cer\t$wer_baseline\t$cer_baseline" >> $TMPDIR/$lang.dat
	done
	cat results.gnu | sed "s/%LANG%/$lang/g" > $TMPDIR/$lang.gnu
	gnuplot $TMPDIR/$lang.gnu
done

pdfjoin --nup 2x4 /tmp/*.pdf -o ../graphics/results.pdf
