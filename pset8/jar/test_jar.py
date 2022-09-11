from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(34)
    assert jar.capacity == 34
    assert jar.size == 0
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(12)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(3)
    assert jar.size == 4
    jar.deposit(8)
    assert jar.size == 12


def test_withdraw():
    jar = Jar(20)
    jar.deposit(19)
    jar.withdraw(4)
    assert jar.size == 15
    jar.withdraw(6)
    assert jar.size == 9
    jar.withdraw(8)
    assert jar.size == 1