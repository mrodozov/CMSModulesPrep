for i in `ls modulescache`;
do
    for j in `ls modulescache/$i`;
    do
	if [[ `cat modulescache/$i/$j/CMS_*.log | grep  error: | wc -l` > 0 ]]; then
	    echo $i/$j; cat modulescache/$i/$j/CMS_*.log | grep  error: | wc -l;
	fi;
    done;
done
