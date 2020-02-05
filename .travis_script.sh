if [[ $TRAVIS_EVENT_TYPE == "push" && $TRAVIS_BRANCH == "master" ]] ; then
  for folder in examples/*/ ; do
    for file in "$folder"/* ; do
    if [[ $file == *.py ]] ; then
      python "$file"
      if [[ $? != 0 ]]; then exit 1 ; fi
    fi
    done
  done
fi