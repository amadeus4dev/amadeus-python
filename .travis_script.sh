if if [[ $TRAVIS_PYTHON_VERSION == '3.6.3' ]]; then
  if [[ $TRAVIS_EVENT_TYPE == "push" && $TRAVIS_BRANCH == "master" ]] ; then
    for folder in examples/*/ ; do
      for file in "$folder"/* ; do
        if [[ $file == *.py ]]
        then
          python "$file" && echo "done"
        fi
      done
    done
  fi
  if [[ $TRAVIS_EVENT_TYPE == "push" && $TRAVIS_BRANCH == "master" ]] ; then
    for folder in examples/*/ ; do
      for file in "$folder"/* ; do
        if [[ $file == *.py ]]
        then
          python "$file"
        fi
      done
    done
  fi
fi