from langchain_ollama import OllamaLLM

if __name__ == '__main__':
    model = OllamaLLM(model="player")
    print(model.invoke("""
    instructions: ```
        Welcome to My Space Adventure

        You wake up on a space station.

        The Closet
        You are in a small nondescript closet.

        Here are the exits: 
        n

        You see the following: 
        shelf
        uniform
    ```"""))