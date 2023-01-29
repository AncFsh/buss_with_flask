from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("kontakt.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/contact")

@app.route('/mypage/me')
def me():
    return render_template("kontakt_2.html")

if __name__ == '__main__':
    app.run(debug = True)