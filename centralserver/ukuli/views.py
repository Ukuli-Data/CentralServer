from flask import render_template, request 

@datamonger.route('/') 
@datamonger.route('/hello') 
def daya_cruncher(): 
    user = request.args.get('user', 'Tomi') 
    return render_template('index.html', user=user) 
