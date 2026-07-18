Read the Apache-style access log at `/app/access.log` and create a UTF-8 JSON report at `/app/report.json`.

Ignore blank lines. Treat every nonblank line as one request. The client IP is the first whitespace-delimited field. Extract the requested path from the quoted HTTP request between the method and HTTP version. Supported methods are GET, POST, PUT, DELETE, HEAD, and PATCH. If paths tie for the highest count, select the one that appears first in the log.

Success criteria:

1. `/app/report.json` exists, is valid JSON, and contains exactly the keys `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is an integer equal to the number of nonblank request lines.
3. `unique_ips` is an integer equal to the number of distinct client IP addresses.
4. `top_path` is the string path requested most often, using first appearance to break a tie.
