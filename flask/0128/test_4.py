"""testing 실습"""
import unittest
from test_3 import app # Test할 파일에서 flask 앱을 가져옵니다.

class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self) #test를 위한 test client 인스턴스를 생성합니다.
        
        response = tester.get("/",content_type="html/text") #test_3의 루트 url로 GET요청

        self.assertEqual(response.status_code,200) #GET요청 결과가 200(OK)인지 확인

