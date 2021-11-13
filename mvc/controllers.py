import importlib

if __name__ == '__main__':
    view = input("Please input view name: ")
    try:
        module = importlib.import_module(f"views_{view}")
        module.main()
    except ImportError:
        print(f"View not found {view}")
