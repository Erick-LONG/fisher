from flask import current_app

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger,desc,func
from sqlalchemy.orm import relationship

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(15),nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean,default=False)

    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        #根据传入的一组isbn，到Wish表中计算出某个礼物
        #的wish心愿数量
        # db.session 做查询
        # 接收条件表达式
        # mysql in
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched==False,
                                      Wish.isbn.in_(isbn_list),
                                      Wish.status==1).group_by(
                                      Wish.isbn).all()
        pass


    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    #对象代表一个礼物，具体
    #类代表礼物这个事务，他是抽象，不是具体的一个
    @classmethod
    def recent(cls):
        #链式调用
        #主体 query
        #子函数
        #first all
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
