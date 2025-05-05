def log_result(test_name, status, message=""):
    with open("qtest_log.txt", "a") as f:
        f.write(f"{test_name}: {status.upper()} - {message}\n")
