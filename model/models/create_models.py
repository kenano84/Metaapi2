from model.db import db
from model.models.user import User


def main():
    db.create_all()


if __name__ == '__main__':
    main()
