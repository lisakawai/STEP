#plot.pl
set grid
set key right bottom
set ytics 0.1
set xlabel "n"
set ylabel "time(sec)"
set terminal png
set output 'plot.png'
plot 'plot.txt' using 1:2 w l t 'time' lc rgb 'red'
pause(-1)