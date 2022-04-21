import json
import os
import base64
import random
import uuid

from flask import render_template, Markup, request, url_for
from googleapiclient.discovery import build
from google.oauth2 import service_account

from app.app import app

@app.route('/', methods=['GET'])
def home():
    creds = service_account.Credentials.from_service_account_info(
        json.loads(os.getenv("SERVICE_ACCOUNT_INFO")),
        scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'],
    )
    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets().values().get(
        spreadsheetId=os.getenv("SPREADSHEET_ID"),
        range=os.getenv("SPREADSHEET_RANGE"),
    ).execute()['values']

    num_dogs = len(sheet[1]) - 3 # ignore clades, breed and abbrev columns
    norm = int(sheet[num_dogs+2][1]) # ignore title and header row, and norm column

    target = random.randrange(num_dogs)

    similarities = []
    for idx, row in enumerate(sheet[2:num_dogs+2]): # ignore title and header row
        name = row[1]
        if idx == target:
            similarities.append((1.0, name))
        else:
            similarities.append((int(row[3+target])/norm, name))

    similarities.sort()

    prev_similarity = 2
    prev_rank = 0
    ranks = {}
    for idx, (similarity, name) in enumerate(reversed(similarities)):
        if similarity == prev_similarity:
            ranks[name] = prev_rank
        else:
            ranks[name] = idx
            prev_rank = idx
        prev_similarity = similarity

    formatted_choices = {
        name: {"similarity": similarity, "rank": ranks[name]+1}
        for similarity, name in similarities
    }

    return render_template(
        "home.html",
        choices={name: formatted_choices[name] for name in sorted(formatted_choices)},
    )
