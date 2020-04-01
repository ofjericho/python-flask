from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hotels = [
  {
    'hotel_id': 'alpha',
    'name': 'Alpha Hotel',
    'stars': '4.3',
    'value': '314.00',
    'city': 'São Paulo'
  },
  {
    'hotel_id': 'bravo',
    'name': 'Bravo Hotel',
    'stars': '4.8',
    'value': "289.09",
    'city': 'Santa Catarina'
  },
  {
    'hotel_id': 'charlie',
    'name': 'Charlie Hotel',
    'stars': '4.2',
    'value': "490.60",
    'city': 'São Paulo'
  }
]




class Hotels(Resource):
  def get(self):
    return {'hotels': hotels}

class Hotel(Resource):
  arguments = reqparse.RequestParser()
  arguments.add_argument('name')
  arguments.add_argument('stars')
  arguments.add_argument('value')
  arguments.add_argument('city')

  def find_hotel(hotel_id):
    for hotel in hotels:
      if hotel['hotel_id'] == hotel_id:
        return hotel
    return None

  def get(self, hotel_id):
    hotel = Hotel.find_hotel(hotel_id)
    if hotel:
      return hotel
    return {'msg': 'Hotel not found' }, 404

  def post(self, hotel_id):
    data_arguments = Hotel.arguments.parse_args()
    hotel_obj = HotelModel(hotel_id, **data_arguments)
    new_hotel = hotel_obj.json()
    hotels.append(new_hotel)
    
    return new_hotel, 201

  def put(self, hotel_id):
    
    data_arguments = Hotel.arguments.parse_args()
    hotel_obj = HotelModel(hotel_id, **data_arguments)
    new_hotel = hotel_obj.json()
    hotel = Hotel.find_hotel(hotel_id)

    if hotel:
      hotel.update(new_hotel)
      return new_hotel, 200
    hotels.append(new_hotel)
    return new_hotel, 201

  def delete(self, hotel_id):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
    return {'msg':'Hotel deleted'}

    

