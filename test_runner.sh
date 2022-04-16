for test_file in tests/* ;
do
	PYTHONPATH="$PWD/src" python3 "${test_file}"
done
