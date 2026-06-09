import re

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) .* '
    r'"(?P<method>\S+) (?P<endpoint>\S+) .*" '
    r'(?P<status>\d+) .* '
    r'(?P<response>\d+\.\d+)'
)


def parse_log_line(line: str):
    match = LOG_PATTERN.match(line)

    if not match:
        return None

    return {
        "ip_address": match.group("ip"),
        "method": match.group("method"),
        "endpoint": match.group("endpoint"),
        "status_code": int(match.group("status")),
        "response_time": float(match.group("response"))
    }