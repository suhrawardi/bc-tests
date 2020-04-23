# Tests

This library contains the integration tests for a Business Central project.
You need to copy the .env.example file to .env and adapt it with the correct
credentials. If all is well, you can run the tests like:

    ./run.sh

or spin up the tests in a Docker container with:

    docker-compose up

Mind that you need to have the correct Python installed and instal the
requied pacakges with:

    pip install -r requirements.txt
