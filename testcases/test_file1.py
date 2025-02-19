import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome import webdriver


# we automate most of sanity and regresssion testing repetative tests.. not complicated one
## we dont automate functional test cases i.e bva, ecp, drop down,radio btn status check,ui check, database testing do not comes under automation
## we check compulsarily url,login or not,page titles correct or not,data add,update,delete check, search check
## in real time browser are run in headless mode  as it takes less time as compared without headless
## jenkins is used to run,track,ananlysis,handle automation test cases easily.
## you can automate your job also by build trigger

## jenkins->dashboard->new item->enter item name(project folder name)->freestyle project->ok->
# configuration->advanced->use custom workspace->directory(absolute path)->build steps->
# execute windows batch command(pytest)->save->apply->build now

## github->new(+)new repository->repository name->create repository->copy https link->
## open folder project->hit git bash here->git init (command.local to global transfer)
## git remote add origin ( paste generated command)->git config --global user.name "rohit8622"
##git config --global user.email "rohitpanchal750700@gmail.com"->git status(red files i.e not in global repo)->
## git add -A(add file to staging temp file before load to global repo)->git commit -m "first commit"(select files to upload to github repo)->
## git status


# pytest module test file name should start from---> test_
# command---> 1)  pytest  2) pytest -v
#3) pytest --html=Reports/myreport.html  -n=2
#4) pytest --html=Reports/myreport.html -n=2  -m group1 and group2

class Test_py:           #you must have to keep class name first letter capital  cause it give error (empty suite)

    @pytest.mark.group1
    def test_sum_001(self):  #test case start with  (test_)      # test cases (method)
        a = 2
        b = 4
        sum = a + b
        print('sum-->'+str(sum))
        if sum == 6:
            assert True
        else:
            assert False

    # def sum_002_test(self): # # this test case will not consider by pytest
    #     a = 4
    #     b = 4
    #     sum = a + b
    #     print('sum-->' + str(sum))
    #     if sum == 6:
    #         assert True
    #     else:
    #         assert False
    #
    @pytest.mark.group1
    def test_sum_002(self):
        a = 2
        b = 4
        mul = a * b
        print('mul--->'+str(mul))
        if mul ==7:
            assert True
        else:
            assert False
    @pytest.mark.group3
    # def test_credenceurl(self):
    #     # chrome_options=webdriver.ChromeOptions()
    #     # chrome_options.add_argument('headless')
    #     driver=webdriver.Edge()
    #     driver.get('https://credence.in/')
    #     print(driver.title)
    #     if driver.title=='Credence':
    #         print('you are at credence site')
    #         assert True     ## using this u can mark status of test case pass or fail
    #     else:
    #         print('you are at wrong site')
    #         assert False        ##used to raise exceptions intentionally ie mark ur test case as fail
    #     driver.quit()

    @pytest.mark.group4     ## test case will come under both marker
    @pytest.mark.group5
    def test_credence_003(self):
        driver=webdriver.Edge()
        driver.get('https://credence.in/')
        time.sleep(3)
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']" ).click()
        time.sleep(3)
        l=len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        list=[]
        for i in range(1,l+1):
            mobileno=driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a["+str(i)+"]").text      ## only for element  ## not elements
            # print("mobileno--->"+str(i)+"-->"+ str (mobileno))
            list.append(mobileno)
        print(list)

        if "+91 9579064658" in list:
            print('mobileno is present')
            print(list.index("+91 9579064658"))
            assert True
        else:
            print('mobileno is not present')
            assert False
        driver.quit()












