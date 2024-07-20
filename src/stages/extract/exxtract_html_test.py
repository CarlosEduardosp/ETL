# pylint: disable=W0718
from src.drivers.http_requester.http_requester import HttpRequester
from src.drivers.html_collector.html_collector import HtmlCollector
from src.stages.contracts.extract_contract import ExtractContract
from .extract_html import ExtractHtml


def test_extract():
    http_requester = HttpRequester()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()

    assert isinstance(response, ExtractContract)

    print(response)


def test_extract_error():
    http_requester = 'entradaerrada'
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        response = extract_html.extract()
        assert isinstance(response, ExtractContract)
        print(response)
    except Exception as exception:
        print(exception)
