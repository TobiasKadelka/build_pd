export DATALAD_LOG_TRACEBACK=collide
for d in /data/BnB_USER/Kadelka/PD/source_data/* ; do
	for b in $d/* ; do
		datalad hirni-import-dcm $b
	done
done
