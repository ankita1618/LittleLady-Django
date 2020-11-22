# LittleLady-Django

## Instructions

### Installation of Docker on Ubuntu

- [Docker Documentation](https://docs.docker.com/engine/install/ubuntu/)
- The easiest way of installing docker is by using a script :
- Remove the older version of docker
- `$ sudo apt-get remove docker docker-engine docker.io containerd runc`
- [www.get.docker.com](https://get.docker.com/)
- `$ curl -fsSL https://get.docker.com -o get-docker.sh`
- On the home folder, you will get a script file
- `$ sudo sh get-docker.sh`
- `$ docker --version` -> To check if it is installed or not.

### Signup for stripe account

- Signup at [www.stripe.com](https://stripe.com/en-in)
- Then go to the [Dashboard](https://dashboard.stripe.com/test/dashboard).
- Click on 'Get your test API keys'.
- Then open the code folder and go to *djangoProject -> settings.py*
- Fill **STRIPE_SECRET_KEY** = *‘your_sripe_secret_key’*
- Fill **STRIPE_PUBLISHABLE_KEY** = *‘your_stripe_publishable_key’*

### Then add your email ID and Password.

- In the same *settings.py* file.
- Fill **DEFAULT_EMAIL** = *’your_email_id’*
- Fill **EMAIL_PASSWORD** = *’your_password’*
- Two settings to be changed
- Then open your Gmail settings 
- *Settings -> See all settings -> Forwarding and POP/IMAP -> Enable IMAP*
- Go to manage your *Google account -> Security -> Turn on to less secure app access*.
- Or click on [www.myaccount.google.com/security](https://myaccount.google.com/security) -> Turn on to less secure app access.

### Now to run the project.

- Open terminal
- Navigate into the project folder 
- Run two commands to build and up
- `$ docker-compose build`
- `$ docker-compose up`
- Run http://0.0.0.0:8000/ in the browser



---

