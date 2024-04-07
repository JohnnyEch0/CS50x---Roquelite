from components.actions import MultiAttack

def test_roll_hits():
    # Create an instance of the MyClass class
    my_obj = MultiAttack(None, None, None, None, None, None, None, None)

    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0

    # Test case 1: min = 2, max = 5
    for i in range(1000):
        result = my_obj.roll_hits(2, 5)
        # count the results
        if result == 1:
            a += 1
        elif result == 2:
            b += 1
        elif result == 3:
            c += 1
        elif result == 4:
            d += 1
        elif result == 5:
            e += 1
    print(f"2 = {b}, 3 = {c}, 4 = {d}, 5 = {e}")

            
        
        
    assert 1 <= result <= 6, "Test case 1 failed"



    # Add more test cases as needed

# Run the tests
test_roll_hits()