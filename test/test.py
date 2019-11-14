from win10toast_dynamic import ToastNotifier

if __name__ == "__main__":
    # Example
    toaster = ToastNotifier()
    toaster.show_toast(
        "Hello World!!!",
        "Python is 10 seconds awsm!",
        duration=-1)
    #toaster.show_toast(
    #    "Example two",
    #    "Once you start coding in Python you'll hate other languages")
        