from sqlalchemy.orm import sessionmaker
from date_scrapper.models import create_db_connection, create_table, Copyrights


class DateScrapperPipeline(object):
    """Aggregator pipeline for storing scraped items in the database"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates table.
        """
        engine = create_db_connection()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save data in the database."""
        item_class = Copyrights
        record = item_class(**item)
        session = self.Session()

        try:
            session.add(record)
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            raise
        finally:
            session.close()

        return item
