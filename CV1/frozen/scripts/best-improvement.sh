
for lang in br ca cy cv de fr it kab ky tt tr ; do

    echo $lang
    cer_baseline=$(cat ../$lang/LOG.$lang.scratch | grep 'Test - ' | grep -o 'CER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g');
    best_cer=100
    best_model=0
    for model in 1 2 3 4 5; do
	cer=$(cat ../$lang/LOG.$lang.$model | grep 'Test - ' | grep -o 'CER:[^,]\+' | cut -f2 -d':' | sed 's/ *//g');
	if (( $(echo "$cer < $best_cer" |bc -l) )); then
	    best_cer=$cer
	    best_model=$model
	    train_set=$(cat ../$lang/LOG.$lang.$model | grep "Num validated clips to be used in TRAIN" | tr -d ' ' | cut -d":" -f 4);
	fi
    done
    best_diff=$(echo "$cer_baseline - $best_cer" |bc -l)
    echo -e "$lang\t$best_model\t$cer_baseline\t$best_cer\t$best_diff\t$train_set" >> BEST.data
done
sort -nk 6,6 BEST.data
