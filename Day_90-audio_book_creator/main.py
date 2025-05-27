# Command Line tool For Creating an Audio from your PDF files
# Input the PDF file
# use an API to convert to text/Audio
# Save your audio book

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from pypdf import PdfReader

import os

text = ''

load_dotenv()


print('*'*10, 'Welcome to PDF to Audio Converter', '*'*10)

print('_________> This Application converts your pdf to audio book page by page')
print('__________> Input the file name from your Directory relative to where you run the application')
print('__________> Input the page number you wish to be converted')
print('________> Get Your Audio book for the page')

filename = input('Input the relative directory of your pdf file: ')
try:
    page_num = int(input('Input the page number (must be a number): '))
except ValueError:
    print('Page must be a number, terminating........')
    exit()
try:
    reader = PdfReader(filename)

    print(f'This book has {len(reader.pages)}')

    page = reader.pages[page_num]
    text = page.extract_text()
    print(text)

except FileNotFoundError:
    print('Invalid File Path, terminating .........')



elevenlabs = ElevenLabs(
api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text=text[:500],
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",

)

output_path = f'audio_page{page_num}.mp3'
save(audio, output_path)

print(f'Audio successfully saved to {output_path}')
