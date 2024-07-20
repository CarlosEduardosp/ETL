from datetime import date
from src.interfaces.http_requester_interface import HttpRequesterInterface
from src.interfaces.html_collector_interface import HtmlCollectorInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

class ExtractHtml:

    def __init__(self, http_requester: HttpRequesterInterface, html_collector: HtmlCollectorInterface):
        self.__http_requester = http_requester
        self.__http_collector = html_collector

    def extract(self) -> ExtractContract:

        try:
            html_information = self.__http_requester.request_from_page()
            essential_information = self.__http_collector.collect_essential_information(html_information['html'])
            response = ExtractContract(
                raw_informatiom_content=essential_information,
                extraction_date=date.today()
            )

            return response
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
