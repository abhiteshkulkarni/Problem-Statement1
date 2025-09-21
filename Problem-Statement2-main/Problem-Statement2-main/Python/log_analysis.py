from collections import Counter

log_file = "access.log"

with open(log_file, "r") as f:
    logs = f.readlines()

error_404 = [line for line in logs if "404" in line]
print("Total 404_error:", len(error_404))

pages = Counter([line.split()[6] for lin in logs if len(line.split()) > 6])
print("Top 5 requested pages:", pages.most_common(5))

ips = Counter([line.split()[o] for line in logs if len(line.split()) > 0])
print("Top 5 requested IPs:", ips.most_common(5))
