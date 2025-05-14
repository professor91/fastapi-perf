## Fast API

`ab -n 10000 -c 5 http://127.0.0.1:8000/`

Note: If you add concurrency then the actual time taken to serve the request will be ~ (time taken by 1 request) / concurrency

- Basic server a callback that only returns a dict take 1 ms and can serve ~2.9K requests per sec
- Adding the middleware header adds 2.5 ms (total 3.5 ms) and can serve ~1.3K requests per sec
- Adding basic Token Authentication (1.2k Tokens) in middleware adds 0.5ms (total 4ms) and can serve ~1.2K requests per sec
- Basic select query to fetch 1.2k records in the api adds 3.5ms (total 7.5ms) and can serve ~650 requests per sec
- Iterating over those 1.2k records is fine but simply adding them to another list adds 8 fucking ms (total 16ms) and now can serve ~300 requests per sec
- Doing the same as above but with a dictionary now adds 16 more fucking ms (total 24ms) and now can serve ~200 requests per sec
