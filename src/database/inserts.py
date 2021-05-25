from datetime import date

from src import db
from src.database.models import Film, Actor


def populate_films():
    film1 = Film(
        title="Some title special film",
        release_date=date(2011, 7, 13),
        description='asdasdasdwqeq rveac',
        distributed_by='Someone',
        length=120,
        rating=8.1
    )
    film2 = Film(
        title="Some title asd film",
        release_date=date(2012, 12, 13),
        description='asdasdaqwe zvsdwqeq rveac',
        distributed_by='SMamamam',
        length=130,
        rating=7.2
    )
    film3 = Film(
        title="Film3",
        release_date=date(2013, 3, 3),
        description='Film3Film3',
        distributed_by='Someone Film3',
        length=333,
        rating=3.3
    )
    film4 = Film(
        title="Film4",
        release_date=date(2014, 4, 4),
        description='Film4Film4',
        distributed_by='Someone Film4',
        length=444,
        rating=4.4
    )
    film5 = Film(
        title="Film5",
        release_date=date(2015, 5, 5),
        description='Film5Film5',
        distributed_by='Someone Film5',
        length=555,
        rating=5.5
    )

    actor1 = Actor(name="NameActor1", birthday=date(1991, 1, 1), is_active=True)
    actor2 = Actor(name="NameActor2", birthday=date(1992, 2, 2), is_active=False)
    actor3 = Actor(name="NameActor3", birthday=date(1993, 3, 3), is_active=True)
    actor4 = Actor(name="NameActor4", birthday=date(1994, 4, 4), is_active=False)
    actor5 = Actor(name="NameActor5", birthday=date(1995, 5, 5), is_active=True)
    actor6 = Actor(name="NameActor6", birthday=date(1996, 6, 6), is_active=False)

    film1.actors = [actor1, actor2, actor4]
    film2.actors = [actor1, actor5, actor4]
    film3.actors = [actor4, actor2, actor5]
    film4.actors = [actor1, actor2, actor5]
    film5.actors = [actor4, actor2, actor6]
    db.session.add(film1)
    db.session.add(film2)
    db.session.add(film3)
    db.session.add(film4)
    db.session.add(film5)
    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(actor3)
    db.session.add(actor4)
    db.session.add(actor5)
    db.session.add(actor6)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print("Populating")
    populate_films()
    print("Successfully")
