def first_entity_value(entities, entity):
	if entities == {}:
		return None

	val = entities["intent"][0]['value']

	if entity == val:
		return entity


def handle_response(response):
  # print(response)
  entities = response['entities']

  # print(entities)
  weather = first_entity_value(entities, 'get_weather')
  # print(weather)
  calendar = first_entity_value(entities, 'get_calendar')
  news = first_entity_value(entities, 'get_news')

  if weather:
    # We can call the wikidata API using the wikidata ID for more info
    return "Good afternoon. It looks like today will be mostly sunny, with a high of 80 degrees and a low of 70 degrees. Great day for outdoor activities"
  elif news:
      return 'There are 15 breaking news articles today, but none in your area'
  elif calendar:
      return "It looks like you have 4 events today, 2 tomorrow and 3 on Friday"
  else:
      return "No problem, glad I could be of assistance"

