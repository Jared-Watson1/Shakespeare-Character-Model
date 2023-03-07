import openai, os, dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("CURIE_MODEL")


def jared_bot(prompt):
    # mainIdeas = generateMainIdeas(prompt)
    response = openai.Completion.create(
    model=model,
    prompt=prompt,
    temperature=0.6,
    max_tokens=750,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']
    
    return answer

p = ""