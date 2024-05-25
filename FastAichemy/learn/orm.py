from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import registry, relationship

mapper_registry = registry()

# print(mapper_registry.metadata)

Base = mapper_registry.generate_base()


# print(Base)

class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(50))

    address = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address_account'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


SQLALCHEMY_DATABASE_URL = "mysql://root:123456789@127.0.0.1:3306/tortoise"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,
)

mapper_registry.metadata.create_all(engine)