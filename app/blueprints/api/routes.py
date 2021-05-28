from flask import json, request, jsonify
from . import bp as api
from app.blueprints.blog.models import Post
from app.blueprints.product.models import Product


@api.route('/posts', methods=['GET'])
def get_posts():
    """
    [GET] /api/products
    """
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])


@api.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    """
    [GET] /api/products
    """
    post = Post.query.get(id)
    return jsonify(post.to_dict())


@api.route('/posts', methods=['POST'])
def create_post():
    """
    [POST] /api/posts
    """
    post = Post()
    print(request.get_json())
    data = request.get_json()
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict())


@api.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    """
    [PUT] /posts/<id>
    """
    post = Post.query.get(id)
    data = request.get_json()
    post.from_dict(data)
    post.save()
    return jsonify(post.to_dict())


@api.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    """
    [DELETE] /api/posts/<id>
    """
    post = Post.query.get(id)
    post.delete()
    return jsonify([p.to_dict for p in Post.query.all()])




@api.route('/products', methods=['GET'])
def get_products():
    """
    [GET] /api/products
    """
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])


@api.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """
    [GET] /api/products
    """
    product = Products.query.get(id)
    return jsonify(product.to_dict())


@api.route('/products', methods=['POST'])
def create_product():
    """
    [POST] /api/products
    """
    product = Product()
    print(request.get_json())
    data = request.get_json()
    product.from_dict(data)
    product.save()
    return jsonify(post.to_dict())


