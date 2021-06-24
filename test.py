try:
    from app import app
    import unittest
    import pytest

except Exception as e:
    print('modules are missing {} '.format(e))

class flasktest(unittest.TestCase):

    def test_4_newcomment(self):
        tester = app.test_client(self)
        response = tester.get('/newcomment')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
 

    def test_2_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    
    def test_1_comment_section(self):
        tester = app.test_client(self)
        response = tester.get('/comment_section')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)



    

if __name__ == "__main__":
    unittest.main()


