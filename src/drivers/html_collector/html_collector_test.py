# pylint: disable=W9008
"""
html_collector_test
"""
from src.drivers.html_collector.html_collector import HtmlCollector
from src.drivers.mocks.http_requester_mock import mock_request_from_page
#from .http_requester import HttpRequester


def test_collect_essential_information():
    """
    :return: print
    """
    # utilizando o html mock
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essential_information = html_collector.collect_essential_information(http_request_response['html'])

    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert 'name' in essential_information[0]
    assert 'link' in essential_information[0]

    print('testando',essential_information)
