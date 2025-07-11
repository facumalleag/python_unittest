import unittest

import requests
from src.api_client import get_location
from unittest.mock import patch, Mock

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get') # crea nuevas pruebas con codigo de pais por ejemplo. tambien agrega mas parametros a la funcion de getlocation
    def test_get_location_returns_expected_data(self,mock_get,):
        mock_get.return_value.status_code=200
        mock_get.return_value.json.return_value={
            "countryName": "USA",
            "regionName": "FLORIDA",  
            "cityName": "MIAMI",
            "latitude": "37.4223", 
            "longitude": "-122.085",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"USA")
        self.assertEqual(result.get("region"),"FLORIDA")
        self.assertEqual(result.get("city"),"MIAMI")
        #self.assertEqual(result.get("continentCode"),"AH")
        #self.assertEqual(result.get("phoneCodes"),"1")
        #self.assertEqual(result.get("countryCode"),"US")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self,mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda:{
                    "countryName": "USA",
                    "regionName": "FLORIDA",  
                    "cityName": "MIAMI",
                    "latitude": "37.4223", 
                    "longitude": "-122.085",
                    "status_code":"200"
                }
            ),
        ]
        
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"USA")
        self.assertEqual(result.get("region"),"FLORIDA")
        self.assertEqual(result.get("longitude"),"-122.085")
        self.assertEqual(result.get("latitude"),"37.4223")
        self.assertEqual(result.get("city"),"MIAMI")


        