import os
import openai
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def fetch_emails(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        snippet = msg_data.get('snippet', '')
        body = ''
        if 'parts' in msg_data['payload']:
            for part in msg_data['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    body = part['body'].get('data', '')
        emails.append({
            'message_id': msg['id'],
            'thread_id': msg_data['threadId'],
            'subject': subject,
            'snippet': snippet,
            'body': body,
            'received_at': msg_data['internalDate']
        })
    return emails

def embed_text(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

if __name__ == "__main__":
    service = get_gmail_service()
    emails = fetch_emails(service, max_results=10)
    for email in emails:
        text = email['subject'] + " " + email['snippet']
        embedding = embed_text(text)
        print(f"Subject: {email['subject']}")
        print(f"Embedding (first 5 dims): {embedding[:5]}")
        print("---")



