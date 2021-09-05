# Setup instructions

1. Set up virtual environment using

   ```python
   virtualenv env_name -p python3.9
   ```

2. Activate the virtual environment by going to env folder location

   ```python
   source env_name/bin/activate
    ```

   press enter

3. Once the env is activated, go back to the django project directory and install all requirements by running

     ```python
    pip install -r requirements.txt
     ```

4. Set up an env file with your configurations. Attached in the project folder is a `.env.example` to guide you on this.
use <https://djecrety.ir/> to generate a secret key.

5. Once done, run

    ```python
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
    ```

6. Use `python manage.py test` to run tests

## weather api information

This project uses data from a [public weather api](https://www.weatherapi.com/). Kindly generate an api key
from their dashboard and set it in the `.env` file. In case you're having trouble, contact me to set this up.

make a HTTP get request to this endpoint

   /api/locations/{city}/?days={number_of_days}

where `city` is a valid city name on earth.
`number_of_days` should be between 1 and 10.

In case invalid data is provided, a HTTP status code 400 (Bad request) will be return with a relevant error message.
