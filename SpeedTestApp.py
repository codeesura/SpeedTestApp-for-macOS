import speedtest
import rumps
import threading

class CustomSpeedtest(speedtest.Speedtest):
    def __init__(self, progress_callback):
        super().__init__()
        self.progress_callback = progress_callback

    def download(self, callback=None):
        return super().download(callback=self.progress_callback)

    def upload(self, callback=None):
        return super().upload(callback=self.progress_callback)

class SpeedTestApp(rumps.App):
    def __init__(self):
        super(SpeedTestApp, self).__init__("📶", icon="my_icon.png")
        self.menu = [rumps.MenuItem('Speed Test', callback=self.speed_test)]

    def update_title_download(self, progress, total=None, start=False, end=False):
        if total is not None and total > 0:
            percentage = (progress / total) * 100
            self.title = f" Download Test... %{percentage:.1f}"

    def update_title_upload(self, progress, total=None, start=False, end=False):
        if total is not None and total > 0:
            percentage = (progress / total) * 100
            self.title = f" Upload Test... %{percentage:.1f}"

    def speed_test(self, _):
        test_thread = threading.Thread(target=self.run_speed_test)
        test_thread.start()

    def run_speed_test(self):
        st = CustomSpeedtest(progress_callback=self.update_title_download)
        try:
            st.get_best_server()
            self.title = " Download Test..."
            download_speed = round(st.download() / (10**6), 2)
            
            st = CustomSpeedtest(progress_callback=self.update_title_upload)
            self.title = " Upload Test..."
            upload_speed = round(st.upload() / (10**6), 2)

            rumps.notification(title='Internet Speed Test',
                               subtitle='Download and Upload Speeds:',
                               message=f'Download: {download_speed} Mbps\nUpload: {upload_speed} Mbps')

            self.title = f' {download_speed}↓ {upload_speed}↑ Mbps'
        except speedtest.SpeedtestBestServerFailure:
            rumps.notification(title='Internet Speed Test',
                               subtitle='Error:',
                               message='Unable to connect to servers. Please check your internet connection and try again.')
            self.title = "📶"

if __name__ == '__main__':
    SpeedTestApp().run()
