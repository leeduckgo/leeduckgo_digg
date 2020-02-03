from app import app
# app.run(host="0.0.0.0")

if __name__ == '__main__':
	# app.run(host="0.0.0.0", port=1234, debug=True)
	app.run(host="0.0.0.0", debug=True, ssl_context=(
        "server/server-cert.pem",
        "server/server-key.pem")
    )

