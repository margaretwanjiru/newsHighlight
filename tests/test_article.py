import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''

    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('BBC', 'Maggy', 'The business graph in Africa.','A look at various businesses in Africa .','business.com','business.com/7643t94.jpg','2018-04-11T07:57:16Z')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Maggy')
        self.assertEquals(self.new_article.title,'The business graph in Africa.')
        self.assertEquals(self.new_article.description,'A look at various businesses in Africa. ')
        self.assertEquals(self.new_article.url,'business.com')
        self.assertEquals(self.new_article.image,'business.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2018-04-11T07:57:16Z')
