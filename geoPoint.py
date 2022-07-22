from google.cloud import firestore
latitude = 0.0
longitude = 0.0
location = firestore.GeoPoint(latitude, longitude)

print(location)
