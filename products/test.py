from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from django.conf import settings
from django.test import TestCase
from .sqlalchemy_models import User, Base # Assumption for SQLAlchemy models exist. 
from fixtures import customerservice, mealportionplans, racquets,sportswear, supplements, weights

class SQLAlchemyMockDataTests(TestCase):
    fixtures = ['customerservice.yaml','mealportionplans.yaml','racquets.yaml','sportswear.yaml','supplements.yaml','weights.yaml']
    weightdata = ['weights.yaml']
    sportsweardata = ['sportswear.yaml']
    racquetsdata = ['racquets.yaml']
    customerservicedata = ['customerservice.yaml']
    supplementdata = ['supplements.yaml']

   
    def setUp(self):
        # Create SQLAlchemy engine and session
        self.engine = create_engine(settings.DATABASES['DEFAULT']['ENGINE'].replace('django','').replace('+','://'))
        self.session = sessionmaker(bind=self.engine)
        self.sesion = self.Session()
        # Create tables for data rows and columns that does not exist yet.
        Base.metadata.create_all(self.engine)
    
    def EndTest(self):
        self.session.close()
        
    def test_mockdata_loading(self):
        users = self.session.query(User).all()
        self.assertEqual(len(users),3)
        self.assertEqual(users[0].username,"sales",users[0].email,"sales@kdfitness.com")
        self.assertEqual(users[1].username,"customerservice",users[1].email,"customerservice@kdfitness.com")
        self.assertEqual(users[2].username,"dataresearch",users[2].email,"dataresearch@kdfitness.com")
        self.assertEqual(users[3].username,"marketing",users[3].email,"marketing@kdfitness.com")
    
    def test_mockdata_customerservice(self):
        customerservicelst = self.session.query(customerservice).all()
        customerserviceagts = self.sesion.query(customerservicelst).all()
        self.assertEqual(len(customerservicelst),4)
        self.assertEqual(customerserviceagts[0].email,"customerservice@kdfitness.cn")
        self.assertEqual(customerserviceagts[1].email,"custmerservice@kdfitness.sg")
        self.assertEqual(customerserviceagts[2].email,"customerservice@kdftiness.ksa")
        self.assertEqual(customerserviceagts[3].email,"customerservice@kdfitness.ae")
        self.assertEqual(customerserviceagts[4].email,"customerservice@kdfintess.kh")


    def test_mockdata_supplement(self):
        supplementlist = self.session.query(supplements).all()
        supplementcheck = self.session.query(supplementlist).all()
        self.assertEqual(len(supplementcheck),5)
        self.assertEqual(supplementcheck[0].name,"omegathree")
        self.assertEqual(supplementcheck[1].name,"calcium")
        self.assertEqual(supplementcheck[2].name,"multivitamin")
        self.assertEqual(supplementcheck[3].name,"sleeping")
        self.assertEqual(supplementcheck[4].name,"probiotics")
        self.assertEqual(supplementcheck[5].name,"minerals")

    def test_mockdata_sportswear(self):
        sportswearlst = self.session.query(sportswear).All()
        sportwearcheck = self.session.query(sportswearlst).All()
        self.assertEqual(len(sportwearcheck),6)
        self.assertEqual(sportwearcheck[0].name, "runningshirtsmale")
        self.assertEqual(sportwearcheck[1].name, "runningshirtfemale")
        self.assertEqual(sportwearcheck[2].name,"swimwearmale")
        self.assertEqual(sportwearcheck[3].name,"swimwearfemale")
        self.assertEqual(sportwearcheck[4].name,"runningshorts")
        self.assertEqual(sportwearcheck[5].name,"trackpantsmale")
        self.assertEqual(sportwearcheck[6].name,"trackpantsfemale")
    
    def test_mockdata_racquets(self):
        racquetslst = self.session.query(racquets).all()
        racquetscheck = self.session.query(racquetslst).all()
        self.assertEqual(len(racquetscheck),6)
        self.assertEqual(racquetscheck[0],name="tennisracquets")
        self.assertEqual(racquetscheck[1],name="badmintonracquets")
        self.assertEqual(racquetscheck[2],name="squashracquets")
        self.assertEqual(racquetscheck[3],name="pickelballpadels")
        self.assertEqual(racquetscheck[4],name="padlepadels")
        self.assertEqual(racquetscheck[5],name="baseballbats")
        self.assertEqual(racquetscheck[6],name="floorballsticks")
    
    def test_mockdata_mealportionplans(self):
        mealportionplanslst = self.session.query(mealportionplans).all()
        mealportionplancheck = self.session.query(mealportionplanslst).all()
        self.assertEqual(len(mealportionplancheck),4)
        self.assertEqual(mealportionplancheck[0],email="mealplanvegs@kdfitness.com")
        self.assertEqual(mealportionplancheck[1],email="mealplansprotein@kdfitness.com")
        self.assertEqual(mealportionplancheck[2],email="trainingasianplans@kdfitness.com")
        self.assertEqual(mealportionplancheck[3],email="trainingafricanplans@kdfitness.com")
        self.assertEqual(mealportionplancheck[4],email="trainingeuropeanplans@kdfitness.com")
        
    def test_mockdata_weights(self):
        weightlst = self.session.query(weights).all()
        weightchecker = self.session.query(weightlst).all()
        self.assertEqual(len(weightchecker),4)
        self.assertEqual(weightchecker[0],email="kettlebell@kdfitness.com", brand="ironbull")
        self.assertEqual(weightchecker[1],email="dumbbell@kdfitness.com",brand="bowflex")
        self.assertEqual(weightchecker[2],email="barbells@kdfitness.com",brand="eleiko")
        self.assertEqual(weightchecker[3],email="weightplates@kdfitness.com",brand="capbarbell")
        self.assertEqual(weightchecker[4],email="barandhandles@kdfitness.com",brand="rougefitness")
        
        
        
        