from flask import Flask, flash, redirect, render_template, request, session
import os

app=Flask(__name__)

items=[]
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="POST":
        item=request.form.get("item")
        items.append(item)
        print(items)
        #Add to Database
    return render_template("index.html", items=items)

