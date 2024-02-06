import Task_1

def test_output(capsys):
    num_paper = 12
    price_paper = 0.5
    num_pencil = 5
    price_pencil = 0.2

    # Run the script to capture the output
    Task_1.main()
    captured = capsys.readouterr()

    # Check if the output matches the expected output
    expected_output = f"Defterin qiymeti:  {price_paper}  azn\nKarandasin qiymeti:  {price_pencil}  azn\n{num_paper} defter ve {num_pencil} karandasin umumi qiymeti:  {num_paper * price_paper + num_pencil * price_pencil}  azn\n"
    assert captured.out == expected_output
