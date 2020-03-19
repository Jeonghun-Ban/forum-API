from flask import session as web_session
from sqlalchemy.orm.session import sessionmaker

from utils.sqlalchemy import engine
from utils.redis import RedisSession

from app.models import Article


Session = sessionmaker(bind=engine)
session = Session()
redisSession = RedisSession()

def create_board(data, board_Name):
    if 'session' in web_session:
        user_id = redisSession.open_session(web_session['session'])
        if user_id:
            article = Article(
                board = board_Name,
                writer = user_id,
                title = data['title'],
                content = data['content']
            )
            save(article)
            response = {
                'status': 'success',
                'message': 'Successfully Created'
            }
            return response, 201
        else:
            response = {
                'status': 'fail',
                'message': 'Unauthorized'
            }
            return response, 401
    else:
        response = {
            'status': 'fail',
            'message': 'Required Login'
        }
        return response, 400

def get_article_list(board_Name):
    return session.query(Article).filter_by(board=board_Name).all()

def save(data):
    session.add(data)
    session.commit()