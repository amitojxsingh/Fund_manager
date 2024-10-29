# tests/test_models.py
import unittest
from project_files.models import Member, MonthlyAllocation  # Adjust the import according to your project structure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_files.test_data import members_test_data, monthly_allocations_test_data  # Import your test data

class TestModels(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///test_committee_fund.db')
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()
        Member.metadata.create_all(cls.engine)
        MonthlyAllocation.metadata.create_all(cls.engine)

    def test_member_creation(self):
        for member_data in members_test_data:
            with self.subTest(member_data=member_data):
                member = Member(**member_data)
                self.session.add(member)
                self.session.commit()
                self.assertEqual(member.name, member_data["name"])

    def test_monthly_allocation_creation(self):
        for allocation_data in monthly_allocations_test_data:
            with self.subTest(allocation_data=allocation_data):
                allocation = MonthlyAllocation(**allocation_data)
                self.session.add(allocation)
                self.session.commit()
                self.assertEqual(allocation.month, allocation_data["month"])

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

if __name__ == '__main__':
    unittest.main()
