# User Acceptance Test (UAT) Cases

1. User can access the home page and see a welcome message.
2. User can POST `{"a": 2, "b": 3}` to `/add` and receive `{"result": 5}`.
3. If required keys are missing, the app returns an internal error.
4. If non-integer input is used, the app crashes.
5. App can be started locally without issues.
6. All unit tests pass successfully when run.
