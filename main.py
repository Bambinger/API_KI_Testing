import os
import openai
import numpy as np
import API_Key_current

openai.api_key = API_Key_current.current_key()


string = '''
"### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### A query to list the names of the departments which employed more than 10 employees in the last 3 months
SELECT'''

engine_current = "text-davinci-002"

response = openai.Completion.create(
    engine=engine_current,
    prompt=string,
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", ";"]
)

text_file = open(engine_current+".txt", "w")

text_file.write(response.choices[0].text)
text_file.close()
