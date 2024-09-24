import pytest
import webbrowser
import os

# Run the tests and generate the report
pytest.main(["--html=C:\\Users\\amrit\\Downloads\\selenium_testing-main\\report.html"])

# Open the generated HTML report in the default web browser
report_path = 'C:\\Users\\amrit\\Downloads\\selenium_testing-main\\report.html'
if os.path.exists(report_path):
    webbrowser.open(report_path)
else:
    print(f"Report file not found: {report_path}")
