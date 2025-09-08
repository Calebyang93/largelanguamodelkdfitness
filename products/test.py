from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from django.conf import settings
from .sqlalchemy_models import User, Base # Assumption for SQLAlchemy models exist. 
from fixtures import customerservice, mealportionplans, racquets,sportswear, supplements, weights

class SQLAlchemyMockDataTests(TestCase):
    fixtures = ['customerservice.yaml','mealportionplans.yaml','racquets.yaml','sportswear.yaml','supplements.yaml','weights.yaml']
    weights = ['weights.yaml']
    sportswear = ['sportswear.yaml']
    racquets = ['racquets.yam']
    cutomerservice = ['customerservice.yaml']
    supplements = ['supplements.yaml']
   
    def setUp(self):
        # Create SQLAlchemy engine and session
        self.engine = create_engine(settings.DATABASES['DEFAULT']['ENGINE'].replace('django','').replace('+','://'))
        self.session = sessionmaker(bind=self.engine)
        self.sesion = self.Session()
        # Create tables for data rows and columns that does not exist yet.
        Base.metadata.create_all(self.engine)
    
    def EndTest(self):
        self.session.close()
    
    def test_mockdata_customerservice(self):
        customerservicelst = self.session.query(customerservice).all()
        customerserviceagts = self.sesion.query(Customerservicelst).all()
        self.assertEqual(len(customerservicelst),4)
        self.assertEqual(customerserviceagts[0].username,"customerservice@kdfitness.cn")
        self.assertEqual(customerserviceagts[1].username,"custmerservice@kdfitness.sg")
        self.assertEqual(customerserviceagts[2].username,"customerservice@kdftiness.ksa")
        self.assertEqual(customerserviceagts[3].username,"customerservice@kdfitness.ae")
        self.assertEqual(customerserviceagts[4].username,"customerservice@kdfintess.kh")


    def test_mockdata_supplement(self):
        supplements = self.session.query(supplements).all()
        
        self.assertEqual(len(supplements),
        
        