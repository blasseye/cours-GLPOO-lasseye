from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.article import Article
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound

"""""
Ecrire le diagramme de classe complet de notre application Ecrire le diagramme séquence de l’inscription d’un participant.
Ajouter le support des articles et de commandes pour les clients :
    - lister les article 
    - recherche d'un article par nom 
    - ajouter un article au panier 
    - creer une commande (fictive) de votre panier. 
    - afficher vos commande et leur status Ajouter le support des articles pour les acheteurs/administrateurs 
    - Ajouter des articles 
    - Modifier des articles 
    - Supprimer un article 
    - Changer le status d'une commande feature et compléter diagramme de classe avec les feature suivantes:
"""""

class ArticleDAO(DAO):
    """
    Article Mapping DAO
    """

    def  __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Article.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Article).order_by(Article.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str, lastname: str):
        try:
            return self._database_session.query(Article).filter_by(name=name, lastname=lastname)\
                .order_by(Article.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            article = Article(name=data.get('name'), size=data.get('size'), theme=data.get('theme'), color=data.get('color'))
            self._database_session.add(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Article already exists")
        return article

    def update(self, article: Article, data: dict):
        if 'name' in data:
            article.name = data['name']
        if 'size' in data:
            article.size = data['size']
        if 'theme' in data:
            article.theme = data['theme']
        if 'color' in data:
            article.color = data['color']
        try:
            self._database_session.merge(article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return article

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))