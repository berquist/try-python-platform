import os
import json
import platform
from pprint import pprint

results = {
    "architecture": platform.architecture(),
    "machine": platform.machine(),
    "node": platform.node(),
    "platform": platform.platform(),
    "processor": platform.processor(),
    "python_build": platform.python_build(),
    "python_compiler": platform.python_compiler(),
    "python_branch": platform.python_branch(),
    "python_implementation": platform.python_implementation(),
    "python_revision": platform.python_revision(),
    "python_version": platform.python_version(),
    "python_version_tuple": platform.python_version_tuple(),
    "system": platform.system(),
    "version": platform.version(),
    "uname": platform.uname(),
}
if results["system"] == "Darwin":
    results["mac_ver"] = platform.mac_ver()
elif results["system"] == "Windows":
    results["win32_ver"] = platform.win32_ver()
else:
    python_minor_version = int(results["python_version_tuple"][1])
    if python_minor_version >= 10:
        results["freedesktop_os_release"] = platform.freedesktop_os_release()
pprint(results)
with open(os.getenv("TRY_PLATFORM_OUTPUTFILE"), "w") as handle:
    json.write(results, handle, indent=2)
