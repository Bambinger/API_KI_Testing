import os
import openai
import numpy as np


openai.api_key = "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"


string = '''
"### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more than 10 employees in the last 3 months
SELECT'''


response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=string,
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", ";"]
)

text_file = open("ada_output.txt", "w")

text_file.write(response.choices[0].text)
text_file.close()
