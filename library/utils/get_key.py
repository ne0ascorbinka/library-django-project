from django.core.management.utils import get_random_secret_key

def main() -> None:
    key = get_random_secret_key()
    print(key)

if __name__ == "__main__":
    main()