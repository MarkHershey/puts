import json
from datetime import datetime

from puts import json_serial

x = {"time": datetime.now()}
print(json.dumps(x, indent=4, default=json_serial))
