import Task_1

def test_output(capsys):
        # Run the script to capture the output
    Task_1.main()
    captured = capsys.readouterr()

    # Check if the output matches the expected output
    expected_output = f"Defterin qiymeti:  {0.5}  azn\nKarandasin qiymeti:  {0.2}  azn\n{12} defter ve {5} karandasin umumi qiymeti:  {7}  azn\n"
    assert captured.out == expected_output
