from django.test import TestCase
from sqlalchemy.orm import sessionmaker
from .sqlalchemy_models import User, Base 
from django.conf import settings 
from sqlalchemy import create_engine

class SQLAlchemyUnitTests(TestCase):
    def setup(self):
        self.engine = create_engine(settings.DATABASES['default']['ENGINE'].replace('django.','').replace('+','://'))
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)
        
    def EndTest(self):
        self.session.close()
    
    def testCreation_queryUser(self):
        # Creates mock data using SQL Alchemy 
        new_user = User(username="marketingadmin",email="marketingadmin@kdfitness.com")
        self.session.add(new_user)
        self.session.commit()
        # Query using SQLAlchemy for marketingadmin user, salesadmin user, dataresearch
        queried_user = self.sesion.query(User).filter_by(username="marketing")
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email,"marketing@kdfitness.com")
        new_user = User(username="sales",email="sales@kdfitness.com")
        self.session.add(new_user)
        self.session.commit()
        queried_user= self.session.query(User).filter_by(username="sales")
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email,"sales@kdfitness.com")
        new_user = User(username="dataresearch",email="dataresearch@kdfintess.com")
        self.session.add(new_user)
        self.session.commit()
        queried_user = self.session.query(User).filter_by(username="dataresearch")
        self.assertIsNone(queried_user)
        self.assertEqual(queried_user.email,"dataresearch@kdfitness.com")
        
        
    