import functools


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('second', __name__, url_prefix='/second')

@bp.route('/names/')
def names():
    db = get_db()
    artists = db.execute(
        'SELECT DISTINCT artist FROM tracks'
    ).fetchall()
    artist_names = [row['artist'] for row in artists]
    return render_template('names.html', artists=artist_names)


@bp.route('/tracks/')
def all_tracks():
    db = get_db()
    count = str(db.execute('SELECT COUNT(id) FROM tracks').fetchone()[0])
    return render_template('tracks.html', count=count, genre=None)


@bp.route('/tracks/<genre>')
def tracks_by_genre(genre):
    db = get_db()
    count = str(db.execute(
        'SELECT COUNT(tracks.id) FROM tracks JOIN genres ON genres.id = tracks.genre_id WHERE genres.title = ?',
        (genre, )
    ).fetchone()[0])
    return render_template('tracks.html', count=count, genre=genre)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks = db.execute(
        'SELECT title, length_ FROM tracks'
    ).fetchall()
    return render_template('seconds.html', tracks=tracks)


@bp.route('/tracks-sec/statistics/')
def stats():
    db = get_db()
    total, avg = db.execute(
        'SELECT SUM(length), AVG(length) FROM tracks'
    ).fetchone()
    return render_template('stats.html', total=total, avg=round(avg, 2))