import re
from langchain_ollama import OllamaLLM
from game import play
from time import sleep

if __name__ == '__main__':
    model = OllamaLLM(model="player")

    status = 0
    command = ""

    while status == 0:
        
        output, status = play(command)

        print("="*10)
        print(output)
        print("="*10)

        while True:
            result = model.invoke(f"""
            instructions: ```
            {output}
            ```""")
            print('-'*10)
            print(result)
            print('-'*10)

            print(f"'{result}'")
            match_answer = re.findall(r"[dD][oO] ?:?(.*)", result)

            if(match_answer and len(match_answer) > 0):
                command = match_answer[0].strip()
                break

            sleep(0.3)
        
        sleep(0.4)
