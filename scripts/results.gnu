set xrange [0:6]
set xlabel "Layer"
set xtics (1,2,3,4,5)
unset key
set title "Character error rate over number of layers retrained (%LANG%)"
set ylabel "CER (%)"
set yrange [0:100]
set terminal pdf
set output "/tmp/%LANG%.cer.pdf"
plot "/tmp/%LANG%.dat" using 2:4, "/tmp/%LANG%.dat" using 2:6 with lines
set title "Word error rate over number of layers retrained (%LANG%)"
set ylabel "WER (%)"
set yrange [0:1]
set output "/tmp/%LANG%.wer.pdf"
plot "/tmp/%LANG%.dat" using 2:3, "/tmp/%LANG%.dat" using 2:5 with lines
