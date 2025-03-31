# Integration Testing Plan

## Components to Test Together

1. Flask web server and route handlers
2. JSON input from POST request
3. Addition logic function
4. Response formatting
5. Flask test client

## Top 6 Integration Use Cases

1. User visits `/` → Receives 200 OK and welcome message
2. User posts to `/add` with valid input → Receives correct sum
3. Malformed JSON → App returns error (without handling)
4. Missing keys in input → App returns error (without handling)
5. Integration between test client and `/add` route
6. App runs without crashing when routes are hit in sequence.
