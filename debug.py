import pytest
import time

report_folder = "Reports_" + str(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())))

pytest.main([
    #'-m=registration',
    '--alluredir=testReports/' + report_folder
])
