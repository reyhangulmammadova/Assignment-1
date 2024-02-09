import Task_1

def test_output(capsys):
    # Run the script to capture the output
    Task_1.main()
    captured = capsys.readouterr()

    # Check if the output matches the expected output
    expected_output = f"Notebook price: {0.5} azn\nPencil price: {0.2} azn\n{12} notebooks and {5} pencils total price: {7.0} azn\n"
    assert captured.out == expected_output
