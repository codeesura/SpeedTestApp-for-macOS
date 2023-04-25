# SpeedTestApp for macOS

Bu uygulama, Python ve rumps paketini kullanarak macOS menü çubuğunda internet hızınızı ölçmenizi ve göstermenizi sağlar. İnternet hızınızı ölçmek için Ookla'nın Speedtest API'sini kullanır.

## Özellikler

- macOS menü çubuğunda anlık hız testi
- İndirme ve yükleme hızlarını gösterme
- İlerleme bildirimi ile hız testi durumu
- Hız testi sonuçlarını bildirim olarak görüntüleme

## Gereksinimler

- Python 3.6+
- rumps paketi
- speedtest-cli paketi

## Kurulum

1. Repoyu klonlayın veya indirin:

```bash
git clone https://github.com/codeesura/SpeedTestApp-for-macOS.git
```


2. Gerekli paketleri yükleyin:

```bash
pip install rumps speedtest-cli
```


3. Uygulamayı çalıştırın:


```bash
python SpeedTestApp.py
```


## Kullanım

- Menü çubuğunda "📶" simgesini tıklayarak uygulamayı başlatın.
- "Speed Test" öğesini tıklayarak hız testini başlatın.
- İndirme ve yükleme hız testleri sırasında ilerlemenin yüzdesi menü çubuğunda görünecektir.
- Test tamamlandığında, sonuçlar bir bildirimle ve menü çubuğunda gösterilecektir.

## Lisans

MIT Lisansı - Daha fazla bilgi için `LICENSE` dosyasına bakın.

