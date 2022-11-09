from MyMainPackage import SomeMainScript  # 1
from MyMainPackage.SomeMainScript import report_main  # 2
from MyMainPackage.SubPackage import AnotherOne  # 3

SomeMainScript.report_main()  # 1

report_main()  # 2

AnotherOne.sub_report()  # 3
