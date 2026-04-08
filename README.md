CURL COMMANDS TO INSERT
curl -X 'POST' \
  'http://localhost:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Steve",
  "last_name": "Rogers",
  "phonenumber": "1234567890",
  "email": "steve@rogers.com"
}'
