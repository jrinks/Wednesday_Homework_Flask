from . import bp as product
from app import db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Product
from .forms import ProductForm, DeletePostForm


@product.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    title = 'ADD PRODUCT'
    form = ProductForm()
    if request.method == 'POST' and form.validate_on_submit():
        product_name = form.name.data
        product_description = form.description.data
        product_price = form.price.data
        product_image = form.image.data

        new_product = Product(product_name, product_description, product_price, product_image)

        db.session.add(new_product)
        db.session.commit()

        flash(f"You have added  {product_name} to the product table", 'info')

        return redirect(url_for('main.index'))

    return render_template('addproduct.html', form=form)


@product.route('/allproducts')
def allproducts():
    title = 'All Products'
    products = Product.query.all()
   
    return render_template('allproducts.html', products=products)
    



#@product.route('/update_product_info/<product.id>', methods=['GET', 'POST'])
#def product_update(id):
 #   print("this will be the product update page")
    # product = Product.query.get_or_404(id)
    # update_form = ProductForm()
    # if request.method == 'POST' and update_form.validate_on_submit():
    #     product_name = update_form.name.data
    #     product_description = update_form.description.data
    #     product_price = update_form.price.data
    #     product_image = update_form.image.data

    #     product.name = product_name
    #     product.description = product_description
    #     product.price = product_price
    #     product.image = product_image

    #     db.session.commit()
    # flash("Product information for {product.name} has been updated.")

    # return render_template('update_product_info.html', name=product_name, id=id, form=update_form)


# @blog.route('/posts/delete/<int:post_id>', methods=['POST'])
# @login_required
# def post_delete(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author.id != current_user.id:
#         flash("You cannot delete another user's post. Who do you think you are?", "warning")
#         return redirect(url_for('blog.myposts'))
#     form = DeletePostForm()
#     if form.validate_on_submit():
#         db.session.delete(post)
#         db.session.commit()
#         flash(f'{post.title} has been deleted', 'info')
#         return redirect(url_for('blog.myposts'))
#     return redirect(url_for('main.index'))