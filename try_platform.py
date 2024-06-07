import platform
from pprint import pprint

platform_results = {
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
pprint(platform_results)
