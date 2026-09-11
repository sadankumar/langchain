from dotenv import load_dotenv
import os


load_dotenv()



def main() -> None:
    print("Hello from helloworld!")
    print(os.environ.get("OPENAI_API_KEY"))
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("API key loaded successfully")
    else:
        print("API key NOT found")

if __name__ == "__main__":
    main()