# Setup
1. Install Docker Desktop
2. `docker compose up`
3. `docker compose exec api python manage.py migrate`
4. `docker compose exec api python manage.py loaddata testcases.json`
5. http://localhost:8000/admin/ - `admin / password`
6. Manual Testing

```
curl http://localhost:8000/quote/3ee485cc-7c9c-485b-a0f1-baf71cd71d28
curl http://localhost:8000/quote/0a9be26b-0111-465e-8f89-93ac747905b3
curl http://localhost:8000/quote/09590402-2656-41d4-9f91-a5c57907b6aa
curl http://localhost:8000/quote/7e531358-acb1-4027-8aee-f10ff24fae97
```
7. Automated Testing
```
docker compose exec api python manage.py test
```
