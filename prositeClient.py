#!/usr/bin/env python
#
# Author: Behrouz Shamsaei <behrouz.shamsaei@uc.edu>
# Date: Sep 2016
#
import requests
#import csv
#from requests.exceptions import Timeout

class PrositeClient(object):
    """Client class is to connect the prosite server and psi-mod csv file to search2 for motifs.
    :param motifs: List of motifs to be searched.
    :param timeout: API request timeout
    :param retries: Number of times to retry request if timeout received
    """

    # API URLs for searching for motifs
    PROSITE_URL_BASE = 'http://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig='
    PROSITE_URL_LINEAGE = '9606'
    PROSITE_URL_DATA_BASE = 'sp'
    PROSITE_URL_FORMAT = 'json'
    TIMEOUT = 120
    RETRIES = 3

    'http://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?sig=rffl&lineage=9606&db=sp&output=json'
    'http://www.ilincs.org/api/SignatureMeta?filter=%7B%22where%22%3A%7B%22treatment%22%3A%22rffl%22%2C%20%22libraryid%22%3A%22LIB_6%22%7D%7D'
    #PROSITE_URL_FORMAT = '&lineage=9606&db=sp&output=json'


    def __init__(self,
                 timeout=TIMEOUT,
                 retries=RETRIES):

        assert(timeout >= 0)
        self.timeout = timeout or self.TIMEOUT

        assert(isinstance(retries, int) and retries >= 0)
        self.retries = retries or self.RETRIES

    def search_prosite(self, params):
        """Prosite search2 for motif API request

        :param params: motif search2 string
        """

        url = self.PROSITE_URL_BASE + params + '&lineage=' + self.PROSITE_URL_LINEAGE + '&db=' + self.PROSITE_URL_DATA_BASE \
              + '&output=' + self.PROSITE_URL_FORMAT

        response = self._request(url)
        search_result = self._extract_response(response)
        print response.text
        return search_result


    def _request(self, url, params=None):
        """Generic prosite request which attaches meta info (e.g. auth)

        :param url: URL of endpoint
        :param params: GET params of request
        """

        response = requests.get(url,
                                timeout=self.timeout)

        return response


    def _extract_response(self, response):
        """Extract data from api resposne"""
        return response.json()


