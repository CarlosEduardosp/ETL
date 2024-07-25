# pylint: disable=W0718
from src.drivers.tests.http_requesterSpy import HttpRequesterSPY
from src.drivers.tests.html_collectorSpy import HtmlCollectorSPY
from src.stages.contracts.extract_contract import ExtractContract
from .extract_html import ExtractHtml


def test_extract():
    http_requester = HttpRequesterSPY()
    html_collector = HtmlCollectorSPY()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()

    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page()
    assert 'html' in html_collector.collect_essential_information_attribuites
    print(response)


def test_extract_error():
    http_requester = 'entradaerrada'
    html_collector = HtmlCollectorSPY()

    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        response = extract_html.extract()
        assert isinstance(response, ExtractContract)
        assert 'html' in html_collector.collect_essential_information_attribuites

        print(response)
    except Exception as exception:
        print(exception)
