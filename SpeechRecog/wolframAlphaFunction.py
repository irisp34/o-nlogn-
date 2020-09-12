import wolframalpha

#From https://www.geeksforgeeks.org/python-create-a-simple-assistant-using-wolfram-alpha-api/
def DAVIDwolframalpha(text):
    app_id = "TLPAPR-VXEYQKW7AL"
    client = wolframalpha.Client(app_id)
    res = client.query(text)
    answer = next(res.results).text
    return answer

