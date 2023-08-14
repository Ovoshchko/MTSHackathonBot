import openai

context_general = "Если вопрос относится к категории 'Проблемы малого бизнеса', то предложи 3 решения проблемы" \
                  "используя дружелюбный и развернутый контекст, " \
                 "иначе верни слово Нет."
context_MTS = "Какая из услуг сервиса МТС Сотрудники поможет в решении следующей проблемы? Напиши, используя развернутый и мягкий лексикон. Добавь вводные слова на подобии: 'Одним из подходящих способов решения'"
fail_answer = "Нет"
unsuccess_answer = "Try again"

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
