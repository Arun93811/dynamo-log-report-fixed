# Task: Apache Access Log Traffic Summary

Analyze the web traffic logs located at `/app/access.log` and generate a concise summary report saved exactly to `/app/report.json`.

## Requirements
Your solution must parse the file line-by-line and accurately compile the following log statistics:
1. Count the total number of non-empty HTTP request lines.
2. Determine the number of unique client IP addresses sending requests.
3. Identify the most frequently visited page path (the URI resource requested).

## Success Criteria
The produced `/app/report.json` file must contain a single JSON object matching the exact format below:
- The summary report must contain the correct count of total requests (`total_requests`).
- The summary report must contain the correct count of unique client IP addresses (`unique_ips`).
- The summary report must identify the most popular requested page path (`top_path`).

### Expected Schema Output Example
```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
