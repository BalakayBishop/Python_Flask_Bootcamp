import os
from authlib.integrations.flask_client import OAuth
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.secret_key = "supersekrit"
oauth = OAuth(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/google/')
def google():
	# Google Oauth Config
	# Get client_id and client_secret from environment variables
	# For development purpose you can directly put it
	# here inside double quotes
	# GOOGLE_CLIENT_ID = os.environ.get("535445369648-p2fqqd9gatrhrmgjes1loks85cqqhf3p.apps.googleusercontent.com")
	# GOOGLE_CLIENT_SECRET = os.environ.get("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")

	CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
	oauth.register(
		name='google',
		client_id="535445369648-p2fqqd9gatrhrmgjes1loks85cqqhf3p.apps.googleusercontent.com",
		client_secret="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",
		server_metadata_url=CONF_URL,
		client_kwargs={
			'scope': 'openid email profile'
		}
	)

	# Redirect to google_auth function
	redirect_uri = url_for('google_auth', _external=True)
	return oauth.google.authorize_redirect(redirect_uri)


@app.route('/google/auth/')
def google_auth():
	token = oauth.google.authorize_access_token()
	user = oauth.google.parse_id_token(token, nonce='')
	print(" Google User ", user)
	return redirect('/')

if __name__ == '__main__':
	app.run()
	