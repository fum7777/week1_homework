# Customer情報の管理
class Customer:
    # コンストラクタ（初期化メソッド）
    def __init__(self, first_name: str, family_name: str, age: int) -> None:
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full_name取得
    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    # 入場料計算
    def entry_fee(self) -> int:
        if self.age <= 3:  # 3歳以下
            return 0
        elif self.age < 20:  # 20歳未満
            return 1000
        elif self.age < 65:  # 20歳以上65歳未満
            return 1500
        elif self.age < 75:  # 65歳以上75歳未満
            return 1200
        else:  # 75歳以上
            return 500

    # CSV形式出力
    def info_csv(self) -> str:
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    # TSV形式出力(タブ区切り)
    def to_tsv(self) -> str:
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    # PSV形式出力(パイプ区切り)
    def to_psv(self) -> str:
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-1. フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
print("--------------------")

# C-2. 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力
print("--------------------")

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# 料金の計算ルール
# こども料金(20歳未満): 1000円
# おとな料金(20歳以上65歳未満): 1500円
# シニア料金(65歳以上): 1200円

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 500 という値を出力
print("--------------------")

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,500" という値を出力
print("--------------------")

# C-5. 3歳以下の入場料金の無料化
# C-6. 75歳以上の料金区分の追加
# 75歳以上の入場料金は500円にしてください

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 500 という値を出力
print(michelle.entry_fee())  # 0 という値を出力
print("--------------------")

# C-7. 単一顧客の情報取得形式の追加その1
print(ken.to_tsv())
print(tom.to_tsv())
print(ieyasu.to_tsv())
print(michelle.to_tsv())
print("--------------------")

# C-8. 単一顧客の情報取得形式の追加その
print(ken.to_psv())
print(tom.to_psv())
print(ieyasu.to_psv())
print(michelle.to_psv())
print("--------------------")
