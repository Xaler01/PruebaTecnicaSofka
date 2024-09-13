


import pytest
import logging

# Configuración del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas de Compra DemoBlaze"

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    with open("reports/test_execution.log", "r") as log_file:
        log_contents = log_file.read()
        summary.append("<div>Logs:</div>")
        summary.append(f"<pre>{log_contents}</pre>")

