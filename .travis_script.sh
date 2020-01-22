if [[ $TRAVIS_EVENT_TYPE == "pull_request" && $TRAVIS_PULL_REQUEST_BRANCH != "master" ]] ; then
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
        PID=$! && wait $PID && sleep 1
      fi
    done
  done
fi