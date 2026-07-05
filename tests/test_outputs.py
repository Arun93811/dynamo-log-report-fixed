from pathlib import Path
import json

def test_total_requests():
    """
    Verifies the success criterion: "The summary report must contain the correct count of total requests."
    """
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json does not exist"
    
    with open(report_path, "r") as f:
        data = json.load(f)
    
    assert "total_requests" in data, "Key 'total_requests' is missing from the report"
    assert data["total_requests"] == 6, f"Expected 6 total requests, got {data['total_requests']}"

def test_unique_ips():
    """
    Verifies the success criterion: "The summary report must contain the correct count of unique client IP addresses."
    """
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json does not exist"
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    assert "unique_ips" in data, "Key 'unique_ips' is missing from the report"
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, got {data['unique_ips']}"

def test_top_path():
    """
    Verifies the success criterion: "The summary report must identify the most popular requested page path."
    """
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json does not exist"
    
    with open(report_path, "r") as f:
        data = json.load(f)
        
    assert "top_path" in data, "Key 'top_path' is missing from the report"
    assert data["top_path"] == "/index.html", f"Expected top path to be '/index.html', got '{data['top_path']}'"
  
