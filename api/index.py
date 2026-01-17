from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import statistics
from typing import List

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyticsRequest(BaseModel):
    regions: List[str]
    threshold_ms: int

# Embedded telemetry data
TELEMETRY_DATA = [
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 205.02,
    "uptime_pct": 97.377,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 131.63,
    "uptime_pct": 98.317,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 177.01,
    "uptime_pct": 99.422,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 158.44,
    "uptime_pct": 98.581,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 185.71,
    "uptime_pct": 99.468,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 137.59,
    "uptime_pct": 99.394,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 188.74,
    "uptime_pct": 97.25,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 197.24,
    "uptime_pct": 98.278,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 125.35,
    "uptime_pct": 99.073,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 149.41,
    "uptime_pct": 98.258,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 104.36,
    "uptime_pct": 99.457,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 140.83,
    "uptime_pct": 97.856,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 128.92,
    "uptime_pct": 97.3,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 214.41,
    "uptime_pct": 97.65,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 231.4,
    "uptime_pct": 97.821,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 119.73,
    "uptime_pct": 98.554,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 198.62,
    "uptime_pct": 98.264,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 135.1,
    "uptime_pct": 99.113,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 194.91,
    "uptime_pct": 98.125,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 154.07,
    "uptime_pct": 97.936,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 155.64,
    "uptime_pct": 99.066,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 123.86,
    "uptime_pct": 98.005,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 195.99,
    "uptime_pct": 98.795,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 198.11,
    "uptime_pct": 97.57,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 223.51,
    "uptime_pct": 98.344,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 208.26,
    "uptime_pct": 99.133,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 190.5,
    "uptime_pct": 99.097,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 139.44,
    "uptime_pct": 98.133,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 182.64,
    "uptime_pct": 99.217,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 159.3,
    "uptime_pct": 97.626,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 124.16,
    "uptime_pct": 99.1,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 135.39,
    "uptime_pct": 98.027,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 226.37,
    "uptime_pct": 98.302,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 222.16,
    "uptime_pct": 97.372,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 123.08,
    "uptime_pct": 97.184,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 159.77,
    "uptime_pct": 97.152,
    "timestamp": 20250312
  }
]

def calculate_percentile_95(values):
    """Calculate 95th percentile"""
    if not values:
        return 0
    sorted_values = sorted(values)
    index = int(len(sorted_values) * 0.95)
    return sorted_values[min(index, len(sorted_values) - 1)]

def load_telemetry_by_region():
    """Group telemetry data by region"""
    data = {}
    for record in TELEMETRY_DATA:
        region = record['region']
        if region not in data:
            data[region] = []
        data[region].append(record)
    return data

@app.get("/")
def read_root():
    return {
        "message": "eShopCo Analytics Endpoint",
        "status": "operational",
        "endpoints": {
            "POST /analytics": "Analyze telemetry data by region"
        }
    }

@app.post("/analytics")
def analyze_telemetry(request: AnalyticsRequest):
    """
    Analyze telemetry data for specified regions
    
    Request body:
    {
        "regions": ["apac", "emea"],
        "threshold_ms": 183
    }
    
    Returns per-region metrics:
    - avg_latency: mean latency
    - p95_latency: 95th percentile latency
    - avg_uptime: mean uptime
    - breaches: count of records above threshold
    """
    try:
        telemetry_data = load_telemetry_by_region()
        results = {}
        
        for region in request.regions:
            if region not in telemetry_data:
                results[region] = {
                    "avg_latency": 0,
                    "p95_latency": 0,
                    "avg_uptime": 0,
                    "breaches": 0
                }
                continue
            
            region_data = telemetry_data[region]
            latencies = [record['latency_ms'] for record in region_data]
            uptimes = [record['uptime_pct'] for record in region_data]
            
            # Calculate metrics
            avg_latency = statistics.mean(latencies) if latencies else 0
            p95_latency = calculate_percentile_95(latencies)
            avg_uptime = statistics.mean(uptimes) if uptimes else 0
            breaches = sum(1 for lat in latencies if lat > request.threshold_ms)
            
            results[region] = {
                "avg_latency": round(avg_latency, 2),
                "p95_latency": round(p95_latency, 2),
                "avg_uptime": round(avg_uptime, 2),
                "breaches": breaches
            }
        
        return results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing telemetry: {str(e)}")