import servicemanager
import logging
import time
import win32serviceutil
import win32service
import win32event

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyService"
    _svc_display_name_ = "My Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        logging.info("MyService started")
        while True:
            time.sleep(5)
            logging.info("MyService is still running")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    win32serviceutil.HandleCommandLine(MyService)