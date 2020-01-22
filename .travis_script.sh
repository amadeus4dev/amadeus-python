if [[ $TRAVIS_PYTHON_VERSION == '3.6.3' ]]; then
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

if [[ $TRAVIS_PYTHON_VERSION == '3.6.3' ]]; then
echo "proto_sosto"
fi

if [[ $TRAVIS_PYTHON_VERSION == 'py36' ]]; then
echo "deutero_sosto"
fi