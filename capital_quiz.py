def main():
    answer = input("What's the capital of France? ").strip()
    if answer.lower() == "paris":
        print("Correct!")
    else:
        print("Wrong. The capital of France is Paris.")
