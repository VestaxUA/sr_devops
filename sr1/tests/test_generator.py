from sr1.generator import even_odd_generator


def test_even_odd_generator_first_values():
    gen = even_odd_generator()
    result = [next(gen) for _ in range(4)]
    assert result == ["Парне", "Непарне", "Парне", "Непарне"]