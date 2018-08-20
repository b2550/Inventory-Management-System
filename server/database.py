from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Settings(db.Model):
    barcodePrefix = db.Column(db.String)
    allowOrders = db.Column(db.Boolean)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean)
    locked = db.Column(db.Boolean)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String)
    name = db.Column(db.String, nullable=False)
    barcode = db.Column(db.BigInteger, unique=True, nullable=False)  # Code on ID card
    orders = db.relationship('Order', backref='user', lazy=True)
    reservations = db.relationship('Reservation', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('info', 'notice', 'warning', name='NotificationTypes'), nullable=False)
    title = db.Column(db.String)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String, unique=True)  # From an 4-char Code 128 barcode (A-Z,0-9) with 1-char prefix
    status = db.Column(db.Enum('availible', 'unavailible', 'reserved', 'missing', 'archived', name='ItemStatuses'), nullable=False)
    name = db.Column(db.String, nullable=False)
    accessories = db.Column(db.String)
    description = db.Column(db.String)
    notes = db.Column(db.String)  # Notes visible to everyone
    adminNotes = db.Column(db.String)  # Notes that are only visible to the admin
    imgURL = db.Column(db.String)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))  # Order that the item is checked out to
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))


class Type(db.Model):  # Item types
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    items = db.relationship('Item', backref='type', lazy=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderDateTime = db.Column(db.DateTime, nullable=False)
    returnDate = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('draft', 'active', 'returned', 'incomplete', name='OrderStatuses'), nullable=False)
    items = db.relationship('Item', backref='order', lazy=True)
    userNote = db.Column(db.String)
    note = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservationDateTime = db.Column(db.DateTime, nullable=False)
    orderDateTime = db.Column(db.DateTime, nullable=False)  # Does not copy. Only used to prevent conflicts.
    returnDate = db.Column(db.Date, nullable=False)
    userNote = db.Column(db.String)  # Note from the user
    note = db.Column(db.String)  # Note from admin that will also convert to notification
    status = db.Column(db.Enum('pending', 'approved', 'change', 'denied'), nullable=False)
    items = db.relationship('Item', backref='reservation', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class APIkey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    key = db.Column(db.String, nullable=False, unique=True)