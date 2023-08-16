import openai
from Files.Texts import *

async def getAnswerForQuestion(message: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\n{context_general}\n{message}\n",
        max_tokens=3000
    )

    answer = response.choices[0].text.strip()

    if answer.__contains__(fail_answer):
        return unsuccess_answer

    return answer

async def findSolutionFromMTS(message: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\n{context_MTS}\n{message}\n",
        max_tokens=3000
    )
    return response.choices[0].text.strip()


async def getInformationAbout(message: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\n{context_information}\n{message}\n",
        max_tokens=3000
    )
    return response.choices[0].text.strip()