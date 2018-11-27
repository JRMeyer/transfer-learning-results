set xrange [0:6]
set yrange [0:100]
set ylabel "CER (%)"
set xlabel "Layer"
set xtics (1,2,3,4,5)
unset key
set title "Character error rate over number of layers retrained (%LANG%)"
set terminal pdf
set output "/tmp/%LANG%.pdf"
plot "/tmp/%LANG%.dat" using 2:4, "/tmp/%LANG%.dat" using 2:6 with lines
