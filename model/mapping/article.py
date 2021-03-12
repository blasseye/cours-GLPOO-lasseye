from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = (UniqueConstraint('name'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    size = Column(String(10), nullable=False)

    theme = Column(String(50), nullable=False)
    color = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Pin's(%s %s %s %s)>" % (self.name, self.size, self.theme, self.color)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "theme": self.theme,
            "color": self.color
        }
