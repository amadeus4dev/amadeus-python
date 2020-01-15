if [[ $TRAVIS_EVENT_TYPE == "pull_request" && $TRAVIS_PULL_REQUEST_BRANCH != "master" ]] ; then
  python samples/ai_generated_photos/ai_generated_photos.py &
  python samples/flight_choice_prediction/flight_choice_prediction.py &
  python samples/flight_offers_search/flight_offers_search.py &
  python samples/hotel_ratings/hotel_ratings.py &
  python samples/points_of_interest/points_of_interest.py &
fi
if [[ $TRAVIS_EVENT_TYPE == "push" && $TRAVIS_BRANCH == "master" ]] ; then
  for folder in samples/*/ ; do
    for file in "$folder"/* ; do
      if [[ $file == *.py ]]
      then
        python "$file"
      fi
    done
  done
fi