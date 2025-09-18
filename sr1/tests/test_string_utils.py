from sr1.string_utils import print_string, analyze_string, uppercase_list


def test_print_string_output(capsys):
    print_string("Привіт")
    captured = capsys.readouterr()
    assert "Привіт" in captured.out


def test_print_string_wrong_type(capsys):
    print_string(123)
    captured = capsys.readouterr()
    assert "Помилка" in captured.out


def test_analyze_string_uppercase(capsys):
    analyze_string("HELLO")
    captured = capsys.readouterr()
    assert "верхньому регістрі" in captured.out


def test_analyze_string_lowercase(capsys):
    analyze_string("hello")
    captured = capsys.readouterr()
    assert "нижньому регістрі" in captured.out


def test_analyze_string_mixed(capsys):
    analyze_string("HeLLo")
    captured = capsys.readouterr()
    assert "великі, так і малі" in captured.out


def test_uppercase_list_correct():
    result = uppercase_list("smogtether")
    assert result == list("SMOGTETHER")


def test_uppercase_list_wrong_type(capsys):
    result = uppercase_list(123)
    captured = capsys.readouterr()
    assert "Помилка" in captured.out
    assert result == []