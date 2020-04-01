class HotelModel:
  def __init__(self, hotel_id, name, stars, value, city):
    self.hotel_id = hotel_id
    self.name = name
    self.stars = stars
    self.value = value
    self.city = city
  
  def json(self):
    return {
      'hotel_id': self.hotel_id,
      'name': self.name,
      'stars': self.stars,
      'value': self.value,
      'city': self.city
    }