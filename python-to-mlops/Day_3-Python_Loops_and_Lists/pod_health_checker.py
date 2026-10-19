# Day 3: Pod Health Checker

pods = [
    {"name": "appbind-be", "status": "Running"},
    {"name": "appprotectt-fe", "status": "CrashLoopBackOff"},
    {"name": "api-model", "status": "Running"},
    {"name": "redis", "status": "Pending"},
]

running_count = 0
problem_count = 0

for pod in pods:
    print("Checking pod:", pod["name"])
    if pod["status"] == "Running":
        print("Status: Healthy")
        running_count += 1
    else:
        print("ALERT: Pod status is", pod["status"])
        problem_count += 1

print("\nTotal pods:", len(pods))
print("Running pods:", running_count)
print("Pods requiring attention:", problem_count)
