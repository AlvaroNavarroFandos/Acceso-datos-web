import tweepy

# Credenciales de autenticación de la API de Twitter
consumer_key = "CbNiNJ3bRgtnIh8Cn0EnRXgIa"
consumer_secret = "InMTexa2ytyRouONa99G86cg07AU1Kdnedjunn02Wo0woMcqe8"
access_token = "401550837-XVuRL4DlEeHMwKmSg0ReAPtGpBdun9I7VMRFlDv0"
access_token_secret = "Th8ipAdRbDZ0ETVikaBIZNALbDnj2J89nwWEt7Vu4pwuO"

# Autenticación en la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crear objeto de la API de Twitter
api = tweepy.API(auth)

# Obtener los seguidores de tu cuenta
cuenta = '@AlvaritoFandos7'
followers = api.get_followers(screen_name= cuenta)

# Mostrar los seguidores en pantalla
print("Seguidores de tu cuenta:",cuenta)
for follower in followers:
    print(follower.name)

