# Setup
1. Install Docker Desktop
2. `docker compose up`
3. `docker compose exec api python manage.py migrate`
4. `docker compose exec api python manage.py loaddata testcases.json`
5. http://localhost:8000/admin/
6. `admin / password`



# TODO
- Should there be a cronjob to pre-store quotes?
- We should store state/cost of calculations, if there has no change to the cost structure, then we don't need to re-calculate the quote.
    - Determining a change should not be more costly than re-calculating a quote
        - Re-calculating will do a lookup on all related cost tables. How do we check all of those last updates times without doing the same lookup?
        - Maybe each quote is stored in the DB?
- The individual variables for the pricing algorithm should be easy to modify, ideally without changing or deploying new code. For example, updating flood coverage in New York from 10% to 20% should be a simple task.
- The pricing algorithm should be designed in a way to allows new variables to be easily added. For example, it should be easy to add in hurricane coverage.
- We want to design this in a way that it will be easy to add more states. Eventually we want to add all 50 states, and want to make it easy to do so in the future.
