import openai, persona_prompt, os, colorama
from dotenv import load_dotenv
from time import sleep

colorama.init(autoreset=True)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def serenity_ai():
    chat_history = []

    print("\n" * 130)
    print(colorama.Fore.YELLOW +"Digite seu nome, se não quiser se identificar, tudo bem, apenas aperte enter! :)")
    user_name = input(colorama.Fore.YELLOW + ">>> ").capitalize()
    sleep(1.5)
    print(colorama.Fore.CYAN + """
                                ███████╗███████╗██████╗ ███████╗███╗   ██╗██╗████████╗██╗   ██╗     █████╗ ██╗
                                ██╔════╝██╔════╝██╔══██╗██╔════╝████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝    ██╔══██╗██║
                                ███████╗█████╗  ██████╔╝█████╗  ██╔██╗ ██║██║   ██║    ╚████╔╝     ███████║██║
                                ╚════██║██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║     ╚██╔╝      ██╔══██║██║
                                ███████║███████╗██║  ██║███████╗██║ ╚████║██║   ██║      ██║       ██║  ██║██║
                                ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝

                                                                                                                          
    """)
    sleep(1.5)
    print(colorama.Fore.CYAN + f"Serenity >>> Olá {user_name}!")
    sleep(1)
    print(colorama.Fore.CYAN + "\nSerenity >>> O que você está sentindo?")
    sleep(1)
    print(colorama.Fore.YELLOW + "\nDica: Digite sair para finalizar o chat.")

    user_input = input("\nVocê >>> ")

    chat_history.append({"role": "system", "content": persona_prompt.persona_prompt})
    chat_history.append({"role": "assistant", "content": f"Olá {user_name}, estou aqui para te ajudar!\nO que você está sentindo?"})
    chat_history.append({"role": "user", "content": user_input})
    
    while True:

        if user_input.lower() == 'sair':
            print(colorama.Fore.CYAN + f"\nSerenity >>> Até logo {user_name}! :)")
            break

        for _ in range(1):
            print(colorama.Fore.YELLOW + "\nPensando", end="", flush=True)
            for _ in range(2):
                sleep(0.7)
                print(".", end="", flush=True)
            sleep(0.7)
            print(".")

        response = openai.chat.completions.create(
            model= "gpt-4",
            messages=chat_history,
            temperature=1
        )        

        serenity_response = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": serenity_response})

        print(colorama.Fore.CYAN + f"\nSerenity >>> {serenity_response}")

        sleep(1)
        user_input = input("\nVocê >>> ")
        chat_history.append({"role": "user", "content": user_input})


if __name__ == "__main__":
    serenity_ai()    