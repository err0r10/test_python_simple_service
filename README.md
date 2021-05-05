# test_python_simple_service

1. Copy ```git clone https://github.com/err0r10/test_python_simple_service.git```
2. ```mkdir test_python_simple_service```
3. Build ```docker build -t test_python_simple_service .```
4. Run docker container ```docker run -d -p 5000:5000 test_python_simple_service```
5. Run curl ```curl --location --request POST 'http://127.0.0.1:5000/you' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "YouName"
}'```
