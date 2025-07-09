from io import StringIO
from typing import Tuple

from pyflakes.api import check
from pyflakes.reporter import Reporter


def analyze_code(code: str) -> Tuple[str, bool]:
    """Return pyflakes output and success flag."""
    stdout = StringIO()
    reporter = Reporter(stdout, stdout)
    messages = check(code, filename="<input>", reporter=reporter)
    output = stdout.getvalue()
    return output, messages == 0
