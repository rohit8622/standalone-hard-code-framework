class Test_py:           #you must have to keep class name first letter capital  cause it give error (empty suite)
    def test_sum_004(self):  #test case start with  (test_)      # test cases (method)
        a = 2
        b = 4
        sum = a + b
        print('sum-->'+str(sum))
        if sum == 6:
            assert True
        else:
            assert False

    def test_sum_005(self):
        a = 4
        b = 4
        sum = a + b
        print('sum-->' + str(sum))
        if sum == 6:
            assert True
        else:
            assert False
