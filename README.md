# WanderVoice

## PART 1: Front End

### 1. Project setup

```
npm install
```

### 2. Compile and hot-reload for development

```
npm run serve
```

### 3. Compile and minify for production

```
npm run build
```

### 4. Lint and fix files

```
npm run lint
```

### 5. Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## PART 2: Lambda Functions

### 1. ``signup_service.py``

It is invoked when users try to register from the front end. If the username has never been used and the password satisfies pre-defined format, a successful status code will be returned and a new account will be created. Username and password of the new account will be saved in a DynamoDB database in AWS. Otherwise, an unsuccessful status code will be returned and the user needs to input a different username.

### 2. ``login_service.py``

It is responsible for verifying the username and the password. By searching the database in DynamoDB, the Lambda function will check whether the password is correct for the given username. If correct, users can enter the application, otherwise they need to log in again.

### 3. ``input_process.py``

It is triggered by PUT event of an MP3 file. After receiving the MP3 file, the function will connect to Transcribe client, initialize the transcription job, and define the target S3 bucket for storing the transcribed text. 

### 4. ``chatbot.py``

It is triggered by PUT event of an txt file, the content of which is the transcribed text. The function will call Amadeus and Ticketmaster APIs based on the current timestamp and retrieve real-time data about hotel booking information and upcoming events. Restricted by the usage of those APIs, the current version of application only supports searching within New York City. Second part of $chatbot.py$ implements the chatbot function. Given the searched result mentioned above, this function will call OpenAI API with a prompt to get the response in text.

### 5. ``store_text.py``

After receiving the text format of response. It will connect to AWS Polly client to take the response and change it into voice. We selected the common voice for in-car voice assistant and English as the target language. For the text output, it will be directly passed to the front end; for the audio output, it will be stored in another S3 bucket and fetched by the front end after completion. 
