for folder in samples/*/ ; do
	for file in "$folder"/* ; do
		if [[ $file == *.py ]]
		then
			python "$file"
		fi
	done
done
