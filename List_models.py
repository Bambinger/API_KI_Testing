# This is a sample Python script.

import os
import openai
openai.api_key = "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"

output=openai.Model.list()

text_file = open("model_out.txt", "w")

text_file.write(str(output))
text_file.close()
