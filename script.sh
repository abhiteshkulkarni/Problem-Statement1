mkdir -p certs

openssl req -nodes -x509 -days 365 \
	-newkey rsa:2048 \
	-keyout certs/wisecow.key \
	-out certs/wisecow.crt \
	-subj "/CN=wisecow.local/O=wisecow"
	
