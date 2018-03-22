./specs/run_development_test.sh
fswatch -o amadeus specs | xargs -n1 -I{} ./specs/run_development_test.sh
