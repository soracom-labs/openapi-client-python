import helpers

if __name__ == "__main__":
    config = helpers.get_auth_config()
    print(f"Result: {config.__dict__}")
