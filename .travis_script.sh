if [[ $TRAVIS_EVENT_TYPE == "pull_request" && $TRAVIS_PULL_REQUEST_BRANCH != "master" ]] ; then
  python examples/hotel_search/hotel_search.py
  if [[ $? != 0 ]]; then exit 1 ; fi
  python examples/flight_choice_prediction/flight_choice_prediction.py
  if [[ $? != 0 ]]; then exit 1 ; fi
  python examples/flight_offers_search/flight_offers_search.py
  if [[ $? != 0 ]]; then exit 1 ; fi
  python examples/hotel_ratings/hotel_ratings.py
  if [[ $? != 0 ]]; then exit 1 ; fi
  python examples/points_of_interest/points_of_interest.py
  if [[ $? != 0 ]]; then exit 1 ; fi
fi
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