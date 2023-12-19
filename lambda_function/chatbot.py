import openai
import boto3
import requests
from amadeus import Client


openai.api_key = ''

# Initialize AWS clients
s3_client = boto3.client('s3')
polly_client = boto3.client('polly')
transcribe_client = boto3.client('transcribe')


def chatbot(query):
    input_message = [{'role': 'user', 'content': query}]
    response = openai.ChatCompletion.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=input_message,
    )
    text_response = response['choices'][0]['message']['content']
    # print(text_response)
    return text_response


def event_info(keyword):
    # Ticketmaster API key
    tm_api_key = ''

    # Endpoint for searching events by keyword
    tm_endpoint = 'https://app.ticketmaster.com/discovery/v2/events'

    # Input parameters
    tm_params = {
        'apikey': tm_api_key,
        'city': 'New York',
        'keyword': keyword,
        'size': 2  # Number of events to retrieve
    }

    # Make the API request
    response = requests.get(tm_endpoint, params=tm_params)

    # Parse and print the response
    data = response.json()
    events = data.get('_embedded', {}).get('events', [])
    text = ""
    for event in events:
        text += f"name: {event.get('name', '')}\n"
        text += f"url: {event.get('url', '')}\n"
        text += f"sales: {str(event.get('sales', ''))}\n"
        text += f"dates: {str(event.get('dates', ''))}\n\n"
    return text


def event_scrape():
    keyword_list = ["sports", "music", "museum", "show"]
    event_result = "Event Information:\n"
    for q in keyword_list:
        search = event_info(q)
        if search:
            event_result += search
    return event_result


def hotel_scrape():
    amadeus = Client(
        client_id='',
        client_secret=''
    )

    '''
    Get list of hotels by city code
    '''
    amenity_list = ["SPA", "PARKING", "WIFI"]
    hotel_text = ''
    for amen in amenity_list:
        response = amadeus.reference_data.locations.hotels.by_city.get(cityCode='NYC', amenities=[amen],
                                                                       ratings=["5"]).data
        hotels = response[:min(3, len(response))]
        for hotel in hotels:
            info = {
                "name": hotel.get("name", ""),
                "hotel id": hotel.get("hotelId", ""),
                "rating": hotel.get("rating", ""),
                "amenities": hotel.get("amenities", ""),
                "city": "New York City"
            }
            hotel_text = hotel_text + str(info) + '\n\n'
    return hotel_text


def save_text(text, filename):
    # Define the destination S3 bucket and file names
    destination_bucket = 'output-text-store'
    destination_file_key = f"{filename}.txt"
    s3_client.put_object(Bucket=destination_bucket, Key=destination_file_key, Body=text)


def text2speech(text, filename):
    # Define the destination S3 bucket and file names
    destination_bucket = 'polly-voice-store'
    destination_file_key = f"{filename}.mp3"

    # Fetch the text content

    # Use Amazon Polly to synthesize speech from the text
    response = polly_client.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId='Salli'  # You can choose a different voice IDs too
    )
    audio_data = response['AudioStream'].read()

    # Upload the MP3 audio to the destination S3 bucket
    s3_client.put_object(Bucket=destination_bucket, Key=destination_file_key, Body=audio_data)


def lambda_handler(event, context):
    # fetch input from text input
    bucket = str(event["Records"][0]['s3']['bucket']['name'])
    key = str(event["Records"][0]['s3']['object']['key'])

    file = s3_client.get_object(Bucket=bucket, Key=key)
    filename = key[:key.find(".")]
    query = file['Body'].read().decode('utf-8')

    if key[0] == "1":
        bg_info = hotel_scrape() + event_scrape()
        prompt = "You are an in-car assistant, give the response based on provided information and keep it around 100 words."
        query = bg_info + query + prompt
    else:
        prompt = 'You are an in-car assistant, keep the answer short and within 50 words.'
        query = query + prompt

    # answer given by chatbot
    answer = chatbot(query)

    # save text in S3
    save_text(answer, filename)

    # convert text into speech
    text2speech(answer, filename)
